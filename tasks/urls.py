from django.urls import path

from .views import create_task, DeleteTask, task_list, home

app_name = 'tasks'

urlpatterns = [
    path('', home , name = 'home'),
    path('/tasks_list', task_list, name='task_list'),
    path('new/', create_task, name='createnewtask'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='deletetask'),

]
