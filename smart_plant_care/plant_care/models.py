from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=80, default="Balcony Plant")
    species = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=120, default="Korea Balcony")
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="plants/", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class SensorReading(models.Model):
    class Source(models.TextChoices):
        MOCK = "mock", "Mock data"
        DEVICE = "device", "STM32 / 51 device"

    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
        related_name="sensor_readings",
    )
    recorded_at = models.DateTimeField()
    soil_moisture = models.PositiveSmallIntegerField(help_text="Percentage: 0-100")
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    light_intensity = models.PositiveIntegerField(help_text="Lux")
    source = models.CharField(max_length=10, choices=Source.choices, default=Source.MOCK)

    class Meta:
        ordering = ["-recorded_at"]

    def __str__(self):
        return f"{self.plant} · {self.recorded_at:%Y-%m-%d %H:%M}"

    @property
    def needs_watering(self):
        return self.soil_moisture < 35


class DiaryEntry(models.Model):
    class Condition(models.TextChoices):
        HEALTHY = "healthy", "Healthy / 건강 / 健康"
        ATTENTION = "attention", "Needs attention / 주의 / 需注意"
        RECOVERING = "recovering", "Recovering / 회복 중 / 恢复中"

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="diary_entries")
    observed_on = models.DateField()
    condition = models.CharField(
        max_length=20,
        choices=Condition.choices,
        default=Condition.HEALTHY,
    )
    soil_moisture = models.PositiveSmallIntegerField(null=True, blank=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    light_intensity = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField()
    photo = models.ImageField(upload_to="diary/%Y/%m/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-observed_on", "-pk"]
        verbose_name_plural = "diary entries"

    def __str__(self):
        return f"{self.plant} · {self.observed_on}"


class WateringEvent(models.Model):
    class Mode(models.TextChoices):
        AUTOMATIC = "automatic", "Automatic"
        MANUAL = "manual", "Manual"
        SIMULATION = "simulation", "Simulation"

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="watering_events")
    watered_at = models.DateTimeField()
    mode = models.CharField(max_length=12, choices=Mode.choices, default=Mode.SIMULATION)
    duration_seconds = models.PositiveSmallIntegerField(default=5)
    successful = models.BooleanField(default=True)

    class Meta:
        ordering = ["-watered_at"]

    def __str__(self):
        return f"{self.plant} · {self.get_mode_display()} · {self.watered_at:%Y-%m-%d %H:%M}"
