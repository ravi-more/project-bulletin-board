from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Projectinfo(models.Model):
    branch_choices = (
        ("Computer Engineering", "Computer Engineering"),
        ("E&TC Engineering", "E&TC Engineering"),
        ("Electronics Engineering", "Electronics Engineering"),
        ("Mechanical Engineering", "Mechanical Engineering"),
        ("Information Technology", "Information Technology"),
        ("Civil Engineering", "Civil Engineering"),
    )
    status_choices = (
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Pending", "Pending"),
    )
    #reccommended_choices = (("Yes", "Yes"), ("No", "No"))
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Roll_Number_and_Names = models.TextField()
    Submitted_Date = models.DateTimeField(default=timezone.now)
    Year = models.CharField(max_length=20, default=datetime.now().year)
    Department = models.CharField(max_length=200, choices=branch_choices)
    status = models.CharField(max_length=20, default="Pending", choices=status_choices)
    #Recommended = models.CharField(
    #    max_length=20, default="Not given", choices=reccommended_choices
    #)
    Observations_or_remarks_by_faculty = models.TextField(default="No remark given")
    Name_of_Approval_committee_members = models.TextField(default="")
    Date_of_Approval = models.CharField(max_length=200, default="-")

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("projects-detail", kwargs={"pk": self.pk})


class links(models.Model):
    link_title = models.CharField(max_length=200)
    link = models.TextField()

    def __str__(self):
        return self.link_title

    def get_absolute_url(selt):
        return reverse("previous_projects", kwargs={"pk": self.pk})

