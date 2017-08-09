from django.conf import settings

if settings.APP_NAME == 'ambition_subject_validators':
    from .tests import models
