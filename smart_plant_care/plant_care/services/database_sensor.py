from ..models import SensorReading
from .mock_sensor import MockSensorProvider
from .sensor_provider import SensorSnapshot


class DatabaseSensorProvider:
    """Read device uploads from Django's database, with a safe mock fallback."""

    def __init__(self):
        self.fallback = MockSensorProvider()

    @staticmethod
    def _snapshot(reading):
        return SensorSnapshot(
            recorded_at=reading.recorded_at,
            soil_moisture=reading.soil_moisture,
            temperature=float(reading.temperature),
            light_intensity=reading.light_intensity,
            connected=True,
        )

    def current(self) -> SensorSnapshot:
        reading = SensorReading.objects.filter(source=SensorReading.Source.DEVICE).first()
        return self._snapshot(reading) if reading else self.fallback.current()

    def history(self, points: int = 12) -> list[SensorSnapshot]:
        readings = list(
            SensorReading.objects.filter(source=SensorReading.Source.DEVICE)[:points]
        )
        if not readings:
            return self.fallback.history(points)
        return [self._snapshot(item) for item in reversed(readings)]
