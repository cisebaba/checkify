from django.urls import path
from tasks.views import TaskListView

urlpatterns = [
    path("mine/", TaskListView.as_view(), name="show_my_tasks"),
]
