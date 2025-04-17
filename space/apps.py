from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'space'

    def ready(self):
        import space.signals  # Import signals when app is ready
