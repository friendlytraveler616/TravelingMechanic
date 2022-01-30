from django.apps import AppConfig


class TravelingmechanicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'travelingMechanic'

    def ready(self):
        import travelingMechanic.signals
