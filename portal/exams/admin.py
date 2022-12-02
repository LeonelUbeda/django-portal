from django.contrib import admin
from .models import Biomarker, Exam


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    filter_horizontal = ("biomarkers",)


@admin.register(Biomarker)
class BiomarkerAdmin(admin.ModelAdmin):
    pass
