from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = 'Get all users.'

    def handle(self, *args, **options):
        users = User.objects.all()
        self.stdout.write(f'{users}')
