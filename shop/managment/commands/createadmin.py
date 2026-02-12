from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Kreira admin usera'

    def handle(self, *args, **options):
        User = get_user_model()
        
        username = os.getenv('ADMIN_USERNAME')
        email = os.getenv('ADMIN_EMAIL')
        password = os.getenv('ADMIN_PASSWORD')
        
        if not password:
            self.stdout.write('ADMIN_PASSWORD nije postavljen!')
            return
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(f'✅ Admin "{username}" kreiran!')
        else:
            self.stdout.write(f'Admin "{username}" već postoji')