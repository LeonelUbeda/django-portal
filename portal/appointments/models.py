from django.db import models

# Create your models here.
from portal.users.models import User
from portal.exams.models import Exam


class Location(models.Model):
    name = models.CharField(max_length=255)


class Appointment(models.Model):

    user = models.ForeignKey(
        User, related_name="user", null=False, blank=False, on_delete=models.CASCADE
    )
    date = models.DateTimeField(null=False, blank=False)
    exams = models.ManyToManyField(
        Exam,
        blank=False,
    )

    def __str__(self) -> str:
        return f"{self.user.username} - {self.date}"
