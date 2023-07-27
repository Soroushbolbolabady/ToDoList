from django.urls import path
from .views import TaskList , TaskCreate

app_name = "api"



urlpatterns = [
    path("tasks_list/" , TaskList.as_view(), name="task_list" ),
    path("new/", TaskCreate.as_view(), name="createnewtask" ),
    
]