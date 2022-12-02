from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ExamsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portal.exams'
    verbose_name: str = _("Exams")
    
