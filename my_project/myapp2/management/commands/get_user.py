from django.core.management.base import BaseCommand, CommandError
from myapp2.models import User


class Command(BaseCommand):
    help = 'Get user by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
