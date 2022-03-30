from django.urls import path
from tasks.views import TaskListView, TaskUpdateView

urlpatterns = [
    path("mine/", TaskListView.as_view(), name="show_my_tasks"),
    path("<int:pk>/complete/", TaskUpdateView.as_view(), name="complete_task"),
]
