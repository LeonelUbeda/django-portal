from django.db import models


class Biomarker(models.Model):
    name = models.CharField(null=False, max_length=255)
    short_name = models.CharField(null=True, max_length=100, blank=True)
    code = models.CharField(null=False, max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name


class Exam(models.Model):
    name = models.CharField(null=False, max_length=255)
    short_name = models.CharField(null=True, max_length=100, blank=True)
    code = models.CharField(null=False, max_length=30)
    biomarkers = models.ManyToManyField(Biomarker, related_name="exam", blank=True)

    def __str__(self) -> str:
        return self.name
