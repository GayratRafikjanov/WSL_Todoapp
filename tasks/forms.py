from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={"placeholder": "Enter title"}),
    )

    description = forms.CharField(
        max_length=40,
        widget=forms.Textarea(attrs={"placeholder": "Enter description"}),
    )

    class Meta:
        model = Task
        fields = ["title", "description", "is_completed"]
