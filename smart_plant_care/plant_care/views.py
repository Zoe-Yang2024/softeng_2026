import json
import secrets

from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import DiaryEntryForm
from .models import DiaryEntry, Plant, SensorReading, WateringEvent
from .services.sensor_provider import get_sensor_provider


def home(request):
    return render(request, "plant_care/home.html")


def get_demo_plant():
    plant, _ = Plant.objects.get_or_create(
        name="My Balcony Plant",
        defaults={
            "location": "Korea Balcony",
            "description": "Smart Plant Care presentation plant",
        },
    )
    return plant


def dashboard(request):
    plant = get_demo_plant()
    provider = get_sensor_provider()
    snapshot = provider.current()
    history = provider.history(points=12)
    last_watering = plant.watering_events.first()
    chart_data = {
        "labels": [item.recorded_at.strftime("%H:%M") for item in history],
        "moisture": [item.soil_moisture for item in history],
        "temperature": [item.temperature for item in history],
        "light": [item.light_intensity for item in history],
    }
    return render(
        request,
        "plant_care/dashboard.html",
        {
            "plant": plant,
            "snapshot": snapshot,
            "last_watering": last_watering,
            "chart_data": chart_data,
        },
    )


@require_POST
def simulate_watering(request):
    plant = get_demo_plant()
    WateringEvent.objects.create(
        plant=plant,
        watered_at=timezone.now(),
        mode=WateringEvent.Mode.SIMULATION,
        duration_seconds=5,
        successful=True,
    )
    messages.success(
        request,
        "Simulation complete · 모의 급수가 완료되었습니다 · 模拟浇水已完成",
    )
    return redirect("plant_care:dashboard")


def diary_list(request):
    plant = get_demo_plant()
    entries = plant.diary_entries.all()
    return render(
        request,
        "plant_care/diary_list.html",
        {"plant": plant, "entries": entries},
    )


def diary_create(request):
    plant = get_demo_plant()
    if request.method == "POST":
        form = DiaryEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.plant = plant
            entry.save()
            messages.success(
                request,
                "Diary saved · 관찰 일지가 저장되었습니다 · 观察日记已保存",
            )
            return redirect("plant_care:diary-list")
    else:
        form = DiaryEntryForm()
    return render(
        request,
        "plant_care/diary_form.html",
        {"plant": plant, "form": form},
    )


def about(request):
    return render(request, "plant_care/about.html")


def _number(payload, key, *, minimum=None, maximum=None):
    try:
        value = float(payload[key])
    except (KeyError, TypeError, ValueError):
        raise ValueError(f"{key} must be a number")
    if minimum is not None and value < minimum:
        raise ValueError(f"{key} must be at least {minimum}")
    if maximum is not None and value > maximum:
        raise ValueError(f"{key} must be at most {maximum}")
    return value


@csrf_exempt
@require_POST
def device_reading_api(request):
    configured_token = settings.DEVICE_API_TOKEN
    if not configured_token:
        return JsonResponse(
            {"ok": False, "error": "Device API is not configured"},
            status=503,
        )

    provided_token = request.headers.get("X-Device-Token", "")
    if not secrets.compare_digest(provided_token, configured_token):
        return JsonResponse({"ok": False, "error": "Unauthorized device"}, status=401)

    try:
        payload = json.loads(request.body or b"{}")
        soil_moisture = _number(payload, "soil_moisture", minimum=0, maximum=100)
        temperature = _number(payload, "temperature", minimum=-40, maximum=85)
        light_intensity = _number(payload, "light_intensity", minimum=0)
    except (json.JSONDecodeError, UnicodeDecodeError, ValueError) as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)

    recorded_at = timezone.now()
    if payload.get("recorded_at"):
        parsed = parse_datetime(str(payload["recorded_at"]))
        if parsed is None:
            return JsonResponse(
                {"ok": False, "error": "recorded_at must be ISO 8601"},
                status=400,
            )
        recorded_at = timezone.make_aware(parsed) if timezone.is_naive(parsed) else parsed

    plant_name = str(payload.get("plant_name") or "My Balcony Plant")[:80]
    plant, _ = Plant.objects.get_or_create(
        name=plant_name,
        defaults={"location": "Korea Balcony"},
    )
    reading = SensorReading.objects.create(
        plant=plant,
        recorded_at=recorded_at,
        soil_moisture=round(soil_moisture),
        temperature=temperature,
        light_intensity=round(light_intensity),
        source=SensorReading.Source.DEVICE,
    )
    return JsonResponse(
        {"ok": True, "reading_id": reading.pk, "message": "Sensor reading stored"},
        status=201,
    )
