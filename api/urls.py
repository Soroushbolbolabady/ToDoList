from django.urls import path
from .views import TaskList

app_name = "api"



urlpatterns = [
    path("taskslist/" , TaskList.as_view(), name="task_list" ),
    
]