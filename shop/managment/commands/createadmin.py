from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Kreira admin usera ako ne postoji'

    def handle(self, *args, **options):
        User = get_user_model()
        
        admin_username = os.getenv('ADMIN_USERNAME', 'admin')
        admin_email = os.getenv('ADMIN_EMAIL', 'admin@nikotrade.com')
        admin_password = os.getenv('ADMIN_PASSWORD')
        
        if not admin_password:
            self.stdout.write(self.style.ERROR('ADMIN_PASSWORD environment varijabla nije postavljena!'))
            return
        
        if not User.objects.filter(username=admin_username).exists():
            User.objects.create_superuser(
                username=admin_username,
                email=admin_email,
                password=admin_password
            )
            self.stdout.write(self.style.SUCCESS(f'Admin user "{admin_username}" kreiran!'))
        else:
            self.stdout.write(f'Admin user "{admin_username}" već postoji')
