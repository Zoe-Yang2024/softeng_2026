import math
from datetime import timedelta

from django.utils import timezone

from .sensor_provider import SensorSnapshot


class MockSensorProvider:
    """Repeatable presentation data that can later be replaced by a device provider."""

    def current(self) -> SensorSnapshot:
        return self.history(points=12)[-1]

    def history(self, points: int = 12) -> list[SensorSnapshot]:
        now = timezone.now().replace(second=0, microsecond=0)
        result = []
        for index in range(points):
            age = points - index - 1
            wave = math.sin(index / 2)
            result.append(
                SensorSnapshot(
                    recorded_at=now - timedelta(hours=age),
                    soil_moisture=max(0, min(100, round(58 - age * 1.4 + wave * 3))),
                    temperature=round(24.3 + wave * 1.2, 1),
                    light_intensity=max(0, round(720 + wave * 210)),
                    connected=True,
                )
            )
        return result
