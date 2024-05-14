from django.core.management.base import BaseCommand
from myapp2.models import User
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Create user.'

    def handle(self, *args, **options):
        user = User(name=fake.name(), email=fake.email(), password=fake.password(), age=random.randint(18, 40))
        ...
        user.save()
        self.stdout.write(f'{user}.')
