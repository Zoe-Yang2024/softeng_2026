from django import forms

from .models import ToDoItem, ToDoList


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ["title"]
        labels = {"title": "목록 이름"}
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "예: 이번 주 할 일", "autofocus": True}
            )
        }


class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ["title", "description"]
        labels = {"title": "할 일", "description": "설명 (선택)"}
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "새 할 일을 입력하세요"}),
            "description": forms.Textarea(
                attrs={"placeholder": "필요한 메모를 적어 주세요", "rows": 3}
            ),
        }
