from rest_framework import serializers
from tasks.models import Tasks


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ("task" , "is_finished")
