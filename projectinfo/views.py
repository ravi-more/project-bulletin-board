from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Projectinfo, links
from django import forms


# Create your views here.


class linksListView(ListView):
    model = links
    ordering = ["-id"]


class linksUpdateView(LoginRequiredMixin, UpdateView):
    model = links
    fields = ["link_title", "link"]
    success_url = "/previous_projects"


class linkDeleteView(LoginRequiredMixin, DeleteView):
    model = links
    success_url = "/previous_projects"


class linksCreateView(LoginRequiredMixin, CreateView):
    model = links
    fields = ["link_title", "link"]
    success_url = "/previous_projects"


class HomeListView(ListView):
    model = Projectinfo
    template_name = "projectinfo/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["id"]
    queryset = Projectinfo.objects.filter(status="Pending")


class ApprovedProjectsListView(ListView):
    model = Projectinfo
    template_name = "projectinfo/approvedprojects.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["id"]
    queryset = Projectinfo.objects.filter(status="Approved")


def about(request):
    return render(request, "projectinfo/about.html", {"title": "about"})


def help(request):
    return render(request, "projectinfo/help.html", {"title": "about"})


def project(request):
    year = request.GET.get("year")
    department = request.GET.get("department")
    if year is None and department is None:
        context = {"posts": Projectinfo.objects.all().order_by("status", "-id")}
    else:
        context = {
            "posts": Projectinfo.objects.filter(
                Year=year, Department=department
            ).order_by("status", "-id")
        }
    return render(request, "projectinfo/project.html", context)


class ProjectinfoCreateView(CreateView):
    model = Projectinfo
    fields = ["Title", "Description", "Roll_Number_and_Names", "Department"]


class ProjectinfoChangeStatusView(LoginRequiredMixin, UpdateView):
    model = Projectinfo
    fields = ["status"]


class ProjectinfoUpdateView(LoginRequiredMixin, UpdateView):
    model = Projectinfo
    fields = [
        "Title",
        "Description",
        "Roll_Number_and_Names",
        "Department",
        "Observations_or_remarks_by_faculty",
        # "Recommended",
        "Name_of_Approval_committee_members",
        "Date_of_Approval",
    ]


class ProjectinfoDeleteView(LoginRequiredMixin, DeleteView):
    model = Projectinfo
    success_url = "/"


""" # print(fields)
    def form_valid(self,form):
        form.instance.department = self.request.GET.get("department")
        return super().form_valid(form)
        
        Dropping because searching get difficult
class ProjectinfoListView(ListView):
    model = Projectinfo
    template_name = 'projectinfo/project.html'    #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering =['-id']
  """


class ProjectinfoDetailView(DetailView):
    model = Projectinfo
