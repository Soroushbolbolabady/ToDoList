from django.forms import ModelForm
from .models import Tasks


class NewTask(ModelForm):
    class Meta:
        model = Tasks
        fields = ('task',)
