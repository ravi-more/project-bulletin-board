from django.urls import path
from .views import (
    ProjectinfoDetailView,
    HomeListView,
    ProjectinfoCreateView,
    ProjectinfoDeleteView,
    ProjectinfoChangeStatusView,
    ProjectinfoUpdateView,
    ApprovedProjectsListView,
    linksListView,
    linksCreateView,
    linksUpdateView,
    linkDeleteView,
)
from . import views

urlpatterns = [
    path("", HomeListView.as_view(), name="projects-home"),
    path("about/", views.about, name="projects-about"),
    path("help/", views.help, name="projects-help"),
    path("projects/", views.project, name="projects-projects"),
    path("projects/<int:pk>/", ProjectinfoDetailView.as_view(), name="projects-detail"),
    path("projects/new/", ProjectinfoCreateView.as_view(), name="projects-create"),
    path(
        "projects/<int:pk>/delete/",
        ProjectinfoDeleteView.as_view(),
        name="projects-delete",
    ),
    path(
        "projects/<int:pk>/changestatus/",
        ProjectinfoChangeStatusView.as_view(),
        name="projects-changestatus",
    ),
    path(
        "projects/<int:pk>/update/",
        ProjectinfoUpdateView.as_view(),
        name="projects-update",
    ),
    path(
        "approvedprojects/",
        ApprovedProjectsListView.as_view(),
        name="projects-approved",
    ),
    path("previous_projects/", linksListView.as_view(), name="previous-projects"),
    path("link_create/", linksCreateView.as_view(), name="link-create"),
    path(
        "previous_project/<int:pk>/link_update/",
        linksUpdateView.as_view(),
        name="link-update",
    ),
    path(
        "previous_projects/<int:pk>/link_delete/",
        linkDeleteView.as_view(),
        name="link-delete",
    ),
]
