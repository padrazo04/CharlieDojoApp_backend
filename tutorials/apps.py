from django.apps import AppConfig


class TutorialsConfig(AppConfig):
    name = 'tutorials'

    def ready(self):
        # Makes sure all signal handlers are connected
        from tutorials import handlers  # noqa