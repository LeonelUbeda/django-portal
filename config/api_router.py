from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from portal.users.api.views import UserViewSet
from portal.exams.api.views import ExamViewSet
from portal.appointments.api.views import AppointmentViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("exams", ExamViewSet)
router.register("users", UserViewSet)
router.register("appointments", AppointmentViewSet)

app_name = "api"
urlpatterns = router.urls
