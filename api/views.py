from rest_framework.generics import ListAPIView , ListCreateAPIView
from rest_framework import permissions
from tasks.models import Tasks
from .serializers import TaskListSerializer , TaskCreateSerializer
# Create your views here.


class TaskList(ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskCreate(ListCreateAPIView):
    queryset =  Tasks.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self,serializer ):
        serializer.save(user=self.request.user)