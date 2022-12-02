from rest_framework import serializers
from ..models import Appointment
from portal.exams.api.serializers import ExamSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    # exams = ExamSerializer(many=True, read_only=True)

    class Meta:
        model = Appointment
        exclude = ("user",)


class AppointmentFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
