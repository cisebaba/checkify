from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from projects.models import Project, AddNotes
from itertools import chain
from tasks.models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/create.html"
    fields = ["name", "description", "members"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.id])


def search_project(request):
    """search function"""
    if request.method == "POST":
        query_name = request.POST.get("name", None)
        if query_name:
            projects = Project.objects.filter(name__contains=query_name)
            tasks = Task.objects.filter(name__contains=query_name)
            results = chain(projects, tasks)
            return render(
                request,
                "projects/search_project.html",
                {"results": results},
            )

    return render(request, "projects/search_project.html")


class AddNotesCreateView(LoginRequiredMixin, CreateView):
    model = AddNotes
    template_name = "projects/create_notes.html"
    fields = ["note"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.project.id])

    def form_valid(self, form):
        note = form.save(commit=False)
        project_id = self.kwargs["project_id"]
        note.project = Project.objects.get(id=project_id)
        note.save()
        return redirect("show_project", pk=project_id)
