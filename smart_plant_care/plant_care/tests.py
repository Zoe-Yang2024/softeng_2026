from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import TestCase
from django.test import override_settings
from django.utils import timezone
from django.urls import reverse

from .models import DiaryEntry, Plant, SensorReading, WateringEvent
from .services.database_sensor import DatabaseSensorProvider
from .services.sensor_provider import get_sensor_provider


class PlantDataModelTests(TestCase):
    def setUp(self):
        self.plant = Plant.objects.create(name="Balcony Tomato", species="Tomato")

    def test_related_plant_records_can_be_saved(self):
        reading = SensorReading.objects.create(
            plant=self.plant,
            recorded_at=timezone.now(),
            soil_moisture=34,
            temperature=24.5,
            light_intensity=700,
        )
        DiaryEntry.objects.create(
            plant=self.plant,
            observed_on=date.today(),
            notes="New leaf observed.",
        )
        WateringEvent.objects.create(plant=self.plant, watered_at=timezone.now())

        self.assertTrue(reading.needs_watering)
        self.assertEqual(self.plant.diary_entries.count(), 1)
        self.assertEqual(self.plant.watering_events.count(), 1)


class MockSensorProviderTests(TestCase):
    def test_provider_returns_dashboard_ready_data(self):
        provider = get_sensor_provider()
        history = provider.history(points=12)

        self.assertEqual(len(history), 12)
        self.assertTrue(all(0 <= item.soil_moisture <= 100 for item in history))
        self.assertTrue(all(item.light_intensity >= 0 for item in history))
        self.assertEqual(provider.current().connected, True)


class PublicPageTests(TestCase):
    def test_home_renders_bilingual_project_content(self):
        response = self.client.get(reverse("plant_care:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Smart Plant Care System")
        self.assertContains(response, "소프트웨어 개발과 스마트팜")
        self.assertContains(response, "利用软件开发与智慧农场技术")

    def test_navigation_destinations_are_available(self):
        names = [
            "plant_care:dashboard",
            "plant_care:diary-list",
            "plant_care:about",
        ]
        for name in names:
            with self.subTest(name=name):
                self.assertEqual(self.client.get(reverse(name)).status_code, 200)


class DashboardTests(TestCase):
    def test_dashboard_displays_simulated_sensor_data(self):
        response = self.client.get(reverse("plant_care:dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Soil Moisture")
        self.assertContains(response, "Temperature")
        self.assertContains(response, "Light Intensity")
        self.assertContains(response, "SIMULATED LIVE")
        self.assertEqual(len(response.context["chart_data"]["labels"]), 12)

    def test_watering_demo_records_event_and_redirects(self):
        response = self.client.post(reverse("plant_care:simulate-watering"), follow=True)

        event = WateringEvent.objects.get()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(event.mode, WateringEvent.Mode.SIMULATION)
        self.assertContains(response, "模拟浇水已完成")

    def test_watering_demo_rejects_get_requests(self):
        response = self.client.get(reverse("plant_care:simulate-watering"))
        self.assertEqual(response.status_code, 405)


class DiaryPageTests(TestCase):
    def setUp(self):
        self.media_directory = TemporaryDirectory()
        self.addCleanup(self.media_directory.cleanup)
        self.media_override = override_settings(MEDIA_ROOT=self.media_directory.name)
        self.media_override.enable()
        self.addCleanup(self.media_override.disable)

    def test_empty_diary_invites_first_entry(self):
        response = self.client.get(reverse("plant_care:diary-list"))
        self.assertContains(response, "Your plant story starts here")
        self.assertContains(response, "Create First Entry")

    def test_diary_entry_with_photo_can_be_created(self):
        image = SimpleUploadedFile(
            "plant.gif",
            b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;",
            content_type="image/gif",
        )
        response = self.client.post(
            reverse("plant_care:diary-create"),
            {
                "observed_on": "2026-06-19",
                "condition": DiaryEntry.Condition.HEALTHY,
                "soil_moisture": 55,
                "temperature": "24.2",
                "light_intensity": 710,
                "notes": "새 잎이 자랐습니다. 新叶正在生长。",
                "photo": image,
            },
            follow=True,
        )

        entry = DiaryEntry.objects.get()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "观察日记已保存")
        self.assertContains(response, "新叶正在生长")
        self.assertTrue((Path(self.media_directory.name) / entry.photo.name).is_file())

    def test_moisture_above_100_is_rejected(self):
        response = self.client.post(
            reverse("plant_care:diary-create"),
            {
                "observed_on": "2026-06-19",
                "condition": DiaryEntry.Condition.HEALTHY,
                "soil_moisture": 101,
                "notes": "Invalid sensor value",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "请输入 0~100")
        self.assertEqual(DiaryEntry.objects.count(), 0)


class AboutAndDeviceApiTests(TestCase):
    def test_about_page_explains_architecture_and_future_plan(self):
        response = self.client.get(reverse("plant_care:about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "SYSTEM ARCHITECTURE")
        self.assertContains(response, "STM32 / 51")
        self.assertContains(response, "个性化智慧农场")

    def test_device_api_is_disabled_without_server_token(self):
        response = self.client.post(
            reverse("plant_care:device-reading-api"),
            data="{}",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 503)

    @override_settings(DEVICE_API_TOKEN="test-device-token")
    def test_device_api_rejects_wrong_token(self):
        response = self.client.post(
            reverse("plant_care:device-reading-api"),
            data="{}",
            content_type="application/json",
            HTTP_X_DEVICE_TOKEN="wrong-token",
        )
        self.assertEqual(response.status_code, 401)

    @override_settings(DEVICE_API_TOKEN="test-device-token")
    def test_device_api_stores_valid_json_reading(self):
        response = self.client.post(
            reverse("plant_care:device-reading-api"),
            data={
                "plant_name": "Remote Basil",
                "soil_moisture": 48,
                "temperature": 23.7,
                "light_intensity": 680,
                "recorded_at": "2026-06-19T12:30:00+09:00",
            },
            content_type="application/json",
            HTTP_X_DEVICE_TOKEN="test-device-token",
        )
        reading = SensorReading.objects.get()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(reading.source, SensorReading.Source.DEVICE)
        self.assertEqual(reading.plant.name, "Remote Basil")

    def test_database_provider_uses_device_readings(self):
        plant = Plant.objects.create(name="API Plant")
        SensorReading.objects.create(
            plant=plant,
            recorded_at=timezone.now(),
            soil_moisture=44,
            temperature=22.5,
            light_intensity=600,
            source=SensorReading.Source.DEVICE,
        )
        snapshot = DatabaseSensorProvider().current()
        self.assertEqual(snapshot.soil_moisture, 44)


class DemoDataCommandTests(TestCase):
    def test_seed_command_is_repeatable(self):
        call_command("seed_demo_data", verbosity=0)
        call_command("seed_demo_data", verbosity=0)

        self.assertEqual(Plant.objects.filter(name="My Balcony Plant").count(), 1)
        self.assertEqual(DiaryEntry.objects.count(), 2)
        self.assertEqual(WateringEvent.objects.count(), 1)
