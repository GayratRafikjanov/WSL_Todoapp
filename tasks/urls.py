from django.contrib.auth import views as auth_views
from .views import TaskListView
from django.urls import path
from . import views


urlpatterns = [
    path("", views.first_page, name="first_page"),
    path("task_list/", TaskListView.as_view(), name="task_list"),
    path("login/", auth_views.LoginView.as_view(), name="login"),  #  login
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # logout
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    # path("", views.TaskListView.as_view(), name="task_list"),
    path("create/", views.CreateTaskView.as_view(), name="create_task"),
    path(
        "page/<int:page>/",
        views.TaskListView.as_view(),
        name="task_list_paginated",
    ),
    path("update/<int:pk>/", views.UpdateTaskView.as_view(), name="update-task"),
    path("delete/<int:pk>/", views.DeleteTaskView.as_view(), name="delete-task"),
]
