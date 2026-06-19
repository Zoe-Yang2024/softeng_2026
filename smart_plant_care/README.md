# Smart Plant Care System

Remote Monitoring and Automatic Watering for Dormitory Plants

스마트팜 전공과 응용소프트웨어개발 수업을 결합한 식물 원격 모니터링 및 자동 급수 시스템 프로토타입입니다.

智慧农场专业与《应用软件开发》课程相结合的植物远程监测和自动浇水系统原型。

## Features

- Responsive Home, Dashboard, Plant Diary and About pages
- Simulated soil moisture, temperature and light readings
- Native Canvas trend chart without an external CDN
- Simulated WiFi camera view and watering control
- Plant diary with image upload
- Device-token protected JSON endpoint for STM32 / 51 MCU data
- Replaceable mock/database sensor provider
- Django Admin and automated tests

## Local setup

Run these commands inside `smart_plant_care`:

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo_data
python manage.py runserver
```

Open <http://127.0.0.1:8000/>.

## Presentation route

1. Home: explain the problem and course connection.
2. Dashboard: show sensor cards, switch the trend chart and run the watering demo.
3. Diary: show the seeded observations, then add a new entry or photo.
4. About: explain the architecture and future roadmap.

The watering button and camera are presentation simulations. They do not control a physical device.

## Hardware upload API

Set a device token in PowerShell before starting the server:

```powershell
$env:DEVICE_API_TOKEN="replace-with-a-long-random-token"
python manage.py runserver
```

An STM32/51 WiFi module can then send an HTTP request:

```http
POST /api/v1/readings/ HTTP/1.1
Content-Type: application/json
X-Device-Token: replace-with-a-long-random-token

{
  "plant_name": "My Balcony Plant",
  "soil_moisture": 56,
  "temperature": 24.3,
  "light_intensity": 720,
  "recorded_at": "2026-06-19T12:30:00+09:00"
}
```

To make Dashboard use uploaded device readings instead of mock data:

```powershell
$env:SENSOR_PROVIDER_CLASS="plant_care.services.database_sensor.DatabaseSensorProvider"
python manage.py runserver
```

If no device readings exist, the database provider safely falls back to simulated data.

## Tests

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

## Future remote deployment

The Django development server is only for local demonstrations. Before accessing the system from China or another remote network:

1. Deploy with a production server and HTTPS.
2. Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=false` and `DJANGO_ALLOWED_HOSTS`.
3. Use a long random `DEVICE_API_TOKEN` and rotate it if exposed.
4. Add user login before enabling real remote watering.
5. Move from SQLite to PostgreSQL when storing long-term sensor history.
6. Add command acknowledgement and safety limits before connecting a physical pump.

See `.env.example` for the required environment variables. Real secrets, uploaded photos and the local SQLite database are ignored by Git.
