from rest_framework.generics import ListAPIView
from rest_framework import permissions
from tasks.models import Tasks
from .serializers import TaskSerializer
# Create your views here.


class TaskList(ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]