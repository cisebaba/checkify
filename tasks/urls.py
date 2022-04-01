from django.urls import path
from tasks.views import TaskListView, TaskUpdateView, TaskCreateView

urlpatterns = [
    path("mine/", TaskListView.as_view(), name="show_my_tasks"),
    path("<int:pk>/complete/", TaskUpdateView.as_view(), name="complete_task"),
    path("create/", TaskCreateView.as_view(), name="create_task"),
]
