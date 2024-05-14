from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Print Hello world! This is my first command'

    def handle(self, *args, **kwargs):
        self.stdout.write('Hello world!')
