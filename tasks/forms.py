from django import forms
from django.db import models
from django.forms import fields
from .models import Task

class taskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description')