from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.accounts'  # Убедитесь, что путь соответствует текущей структуре

    def ready(self):
        # Импортируем сигналы при запуске приложения
        import app.accounts.signals