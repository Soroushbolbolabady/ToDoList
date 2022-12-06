from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Tasks(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=250)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.task

