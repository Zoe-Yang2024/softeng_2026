from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

from django.conf import settings
from django.utils.module_loading import import_string


@dataclass(frozen=True)
class SensorSnapshot:
    recorded_at: datetime
    soil_moisture: int
    temperature: float
    light_intensity: int
    connected: bool = True

    @property
    def needs_watering(self):
        return self.soil_moisture < 35


class SensorProvider(Protocol):
    def current(self) -> SensorSnapshot: ...

    def history(self, points: int = 12) -> list[SensorSnapshot]: ...


def get_sensor_provider() -> SensorProvider:
    provider_class = import_string(settings.SENSOR_PROVIDER_CLASS)
    return provider_class()
