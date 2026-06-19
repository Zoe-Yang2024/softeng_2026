import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Plant",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default="Balcony Plant", max_length=80)),
                ("species", models.CharField(blank=True, max_length=100)),
                ("location", models.CharField(default="Korea Balcony", max_length=120)),
                ("description", models.TextField(blank=True)),
                ("photo", models.ImageField(blank=True, upload_to="plants/")),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="DiaryEntry",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("observed_on", models.DateField()),
                ("condition", models.CharField(choices=[("healthy", "Healthy / 건강 / 健康"), ("attention", "Needs attention / 주의 / 需注意"), ("recovering", "Recovering / 회복 중 / 恢复中")], default="healthy", max_length=20)),
                ("soil_moisture", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("temperature", models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ("light_intensity", models.PositiveIntegerField(blank=True, null=True)),
                ("notes", models.TextField()),
                ("photo", models.ImageField(blank=True, upload_to="diary/%Y/%m/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("plant", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="diary_entries", to="plant_care.plant")),
            ],
            options={"verbose_name_plural": "diary entries", "ordering": ["-observed_on", "-pk"]},
        ),
        migrations.CreateModel(
            name="SensorReading",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("recorded_at", models.DateTimeField()),
                ("soil_moisture", models.PositiveSmallIntegerField(help_text="Percentage: 0-100")),
                ("temperature", models.DecimalField(decimal_places=1, max_digits=4)),
                ("light_intensity", models.PositiveIntegerField(help_text="Lux")),
                ("source", models.CharField(choices=[("mock", "Mock data"), ("device", "STM32 / 51 device")], default="mock", max_length=10)),
                ("plant", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="sensor_readings", to="plant_care.plant")),
            ],
            options={"ordering": ["-recorded_at"]},
        ),
        migrations.CreateModel(
            name="WateringEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("watered_at", models.DateTimeField()),
                ("mode", models.CharField(choices=[("automatic", "Automatic"), ("manual", "Manual"), ("simulation", "Simulation")], default="simulation", max_length=12)),
                ("duration_seconds", models.PositiveSmallIntegerField(default=5)),
                ("successful", models.BooleanField(default=True)),
                ("plant", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="watering_events", to="plant_care.plant")),
            ],
            options={"ordering": ["-watered_at"]},
        ),
    ]
