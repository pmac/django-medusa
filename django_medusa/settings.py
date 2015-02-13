from django.conf import settings


MEDUSA_COLLECTSTATIC_IGNORE = getattr(settings,
    'MEDUSA_COLLECTSTATIC_IGNORE', [])

MEDUSA_COLLECT_STATIC = getattr(settings,
    'MEDUSA_COLLECT_STATIC', False)
