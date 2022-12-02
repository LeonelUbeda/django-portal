from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import AppointmentSerializer, AppointmentFullSerializer
from ..models import Appointment


class AppointmentViewSet(
    GenericViewSet,
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
):
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer) -> None:
        if self.request.user.is_superuser:
            return serializer.save()
        return serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AppointmentFullSerializer
        return AppointmentSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(user=self.request.user)
