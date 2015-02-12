from django.conf import settings


MEDUSA_COLLECTSTATIC_IGNORE = getattr(settings,
    'MEDUSA_COLLECTSTATIC_IGNORE', []
)
