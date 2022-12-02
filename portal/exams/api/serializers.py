from rest_framework import serializers
from portal.exams.models import Exam


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"


class PublicExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ("name",)
