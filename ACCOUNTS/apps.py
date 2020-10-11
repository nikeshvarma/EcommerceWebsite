from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'ACCOUNTS'

    def ready(self):
        import ACCOUNTS.signals
