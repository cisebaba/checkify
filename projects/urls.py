from django.urls import path
from projects.views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    search_project,
)

urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
    path("create/", ProjectCreateView.as_view(), name="create_project"),
    path("search_project/", search_project, name="search_project"),
]
