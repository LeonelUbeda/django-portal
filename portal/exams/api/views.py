from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from .permissions import IsAdminOrReadOnly
from .serializers import ExamSerializer, PublicExamSerializer
from ..models import Exam


class ExamViewSet(
    GenericViewSet,
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Exam.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return ExamSerializer
        return PublicExamSerializer
