from django.core.management.base import BaseCommand
from myapp2.models import Author, Post
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Generate fake authors and posts.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of iterations of fake data.')

    def handle(self, *args, **options):
        count = options.get('count')
        for i in range(1, count + 1):
            author = Author(name=fake.name(), email=fake.email())
            author.save()
            for j in range(random.randint(1, 5)):
                post = Post(
                    title=fake.sentence(nb_words=5),
                    content=fake.text(max_nb_chars=100),
                    author=author
                )
                post.save()
