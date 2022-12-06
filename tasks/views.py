from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from .models import Tasks
from .forms import NewTask


# Create your views here.

def home(request):
    return render(request, 'tasks/home.html')


@login_required(redirect_field_name="tasks:home", login_url="accounts:signin")
def task_list(request):
    tasks = Tasks.objects.filter(person=request.user).order_by('task')
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks_list.html', context)


@login_required(redirect_field_name="tasks:home", login_url="accounts:signin")
def create_task(request):
    if request.method == 'POST':
        form = NewTask(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.person = request.user
            new_form.save()
            return redirect('tasks:task_list')

    else:
        form = NewTask()
        context = {
            "form": form
        }
        return render(request, 'tasks/createnewtask.html', context)


@method_decorator(login_required, name='dispatch')
class DeleteTask(DeleteView):
    model = Tasks
    template_name = 'tasks/deletetask.html'
    success_url = reverse_lazy("tasks:task_list")
