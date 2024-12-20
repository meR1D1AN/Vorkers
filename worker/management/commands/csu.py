import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Создание админа"

    def handle(self, *args, **options):
        username = os.getenv("ADMIN_USERNAME")
        password = os.getenv("ADMIN_PASSWORD")

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(
                username=username,
            )
            user.set_password(password)
            user.save()

            self.stdout.write(self.style.SUCCESS("Админ создан"))
        else:
            self.stdout.write(self.style.SUCCESS("Админ уже создан"))
