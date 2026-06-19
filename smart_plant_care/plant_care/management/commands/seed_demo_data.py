from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from plant_care.models import DiaryEntry, Plant, WateringEvent


class Command(BaseCommand):
    help = "Create repeatable presentation data for Smart Plant Care."

    def handle(self, *args, **options):
        plant, _ = Plant.objects.get_or_create(
            name="My Balcony Plant",
            defaults={
                "species": "Balcony Herb",
                "location": "Korea Balcony",
                "description": "Smart Plant Care presentation plant",
            },
        )
        today = timezone.localdate()
        entries = [
            {
                "observed_on": today,
                "condition": DiaryEntry.Condition.HEALTHY,
                "soil_moisture": 58,
                "temperature": 24.3,
                "light_intensity": 720,
                "notes": "새 잎이 건강하게 자라고 있습니다. 新叶正在健康生长。",
            },
            {
                "observed_on": today - timedelta(days=3),
                "condition": DiaryEntry.Condition.RECOVERING,
                "soil_moisture": 41,
                "temperature": 25.1,
                "light_intensity": 680,
                "notes": "물을 준 뒤 잎이 다시 생기를 찾았습니다. 浇水后叶片恢复了活力。",
            },
        ]
        created_entries = 0
        for item in entries:
            _, created = DiaryEntry.objects.get_or_create(
                plant=plant,
                observed_on=item["observed_on"],
                notes=item["notes"],
                defaults={key: value for key, value in item.items() if key not in {"observed_on", "notes"}},
            )
            created_entries += int(created)

        _, watering_created = WateringEvent.objects.get_or_create(
            plant=plant,
            watered_at__date=today - timedelta(days=1),
            mode=WateringEvent.Mode.SIMULATION,
            defaults={
                "watered_at": timezone.now() - timedelta(days=1),
                "duration_seconds": 5,
                "successful": True,
            },
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Demo data ready: {created_entries} diary entries and "
                f"{int(watering_created)} watering event created."
            )
        )
