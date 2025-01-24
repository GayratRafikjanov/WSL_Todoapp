from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import TaskForm
from .models import Task


# Create your views here.


def first_page(request):
    return render(request, "tasks/first_page.html")


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form})


def task_list(request, page=1):
    task_list = Task.objects.all()

    paginator = Paginator(task_list, 3)

    page_obj = paginator.get_page(page)

    return render(request, "tasks/task_list.html", {"page_obj": page_obj})


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/update_task.html", {"form_as": form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "tasks/confirm_delete.html", {"task": task})

    # CLASS BASED VIEWS
    # CLASS BASED VIEWS
    # CLASS BASED VIEWS


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    paginate_by = 3
    template_name = "tasks/task_list.html"
    login_url = "/login"


class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create_task.html"
    success_url = reverse_lazy("task_list")


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update_task.html"
    success_url = reverse_lazy("task_list")


class DeleteTaskView(DeleteView):
    model = Task
    template_name = "tasks/confirm_delete.html"
    success_url = reverse_lazy("task_list")
