from django.contrib import admin

from .models import DiaryEntry, Plant, SensorReading, WateringEvent


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ["name", "species", "location", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name", "species", "location"]


@admin.register(SensorReading)
class SensorReadingAdmin(admin.ModelAdmin):
    list_display = [
        "plant",
        "recorded_at",
        "soil_moisture",
        "temperature",
        "light_intensity",
        "source",
    ]
    list_filter = ["source", "plant"]
    date_hierarchy = "recorded_at"


@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ["plant", "observed_on", "condition", "soil_moisture", "temperature"]
    list_filter = ["condition", "plant"]
    search_fields = ["notes", "plant__name"]
    date_hierarchy = "observed_on"


@admin.register(WateringEvent)
class WateringEventAdmin(admin.ModelAdmin):
    list_display = ["plant", "watered_at", "mode", "duration_seconds", "successful"]
    list_filter = ["mode", "successful", "plant"]
    date_hierarchy = "watered_at"
