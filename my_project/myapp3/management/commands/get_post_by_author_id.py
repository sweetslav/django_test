from django.core.management.base import BaseCommand
from myapp2.models import Post, Author


class Command(BaseCommand):
    help = 'Get posts by Authors ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID of author')

    # def handle(self, *args, **options):
    #     pk = options['pk']
    #     author = Author.objects.filter(pk=pk).first()
    #     if author is not None:
    #         posts = Post.objects.filter(author=author)
    #         intro = f'All posts for author: {author.name}\n'
    #         text = '\n'.join(post.content for post in posts)
    #         self.stdout.write(f'{intro}\n\n{text}')

    def handle(self, *args, **options):
        pk = options['pk']
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}\n{text}')