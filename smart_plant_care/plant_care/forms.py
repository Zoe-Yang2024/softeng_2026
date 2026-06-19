from django import forms
from django.utils import timezone

from .models import DiaryEntry


class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = [
            "observed_on",
            "condition",
            "soil_moisture",
            "temperature",
            "light_intensity",
            "notes",
            "photo",
        ]
        labels = {
            "observed_on": "Date / 날짜 / 日期",
            "condition": "Plant condition / 식물 상태 / 植物状态",
            "soil_moisture": "Soil moisture (%) / 토양 수분 / 土壤湿度",
            "temperature": "Temperature (°C) / 온도 / 温度",
            "light_intensity": "Light intensity (lx) / 광도 / 光照强度",
            "notes": "Observation notes / 관찰 메모 / 观察备注",
            "photo": "Plant photo / 식물 사진 / 植物照片",
        }
        widgets = {
            "observed_on": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "오늘의 변화를 기록하세요 · 记录今天的植物变化",
                }
            ),
            "photo": forms.ClearableFileInput(attrs={"accept": "image/*"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.is_bound:
            self.fields["observed_on"].initial = timezone.localdate()
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")

    def clean_soil_moisture(self):
        value = self.cleaned_data.get("soil_moisture")
        if value is not None and value > 100:
            raise forms.ValidationError("Enter a value from 0 to 100. / 0~100 사이로 입력하세요. / 请输入 0~100。")
        return value
