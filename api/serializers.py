from rest_framework import serializers
from tasks.models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ("task","is_finished")