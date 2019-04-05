class DjangoRouter:
    """
    Standart DB for Django
    """
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'web':
            return 'django'
        return None

class AppRouter:
    """
    Standart App Router
    """
    def db_for_write(self, model, **hints):
        return 'archer_home'
