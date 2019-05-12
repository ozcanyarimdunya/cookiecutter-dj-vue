from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add default user for project'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("START".ljust(50, ".")))

        try:
            User.objects.get(username='admin')
        except User.DoesNotExist:
            User.objects.create_superuser(
                pk=0,
                username="admin",
                password="123",
                email="admin@admin.com",
                first_name="Admin",
                last_name="Admin"
            )
        finally:
            self.stdout.write(self.style.SUCCESS(
                "Default user (username: admin, password: 123) created".ljust(50, ".")
            ))

        self.stdout.write(self.style.SUCCESS("FINISH".ljust(50, ".")))
