from django.apps import AppConfig


class FolioConfig(AppConfig):
    name = 'folio'

def ready(self):
    import folio.signals