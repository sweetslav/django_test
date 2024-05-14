from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import Author, Post


def hello(request):
    return HttpResponse("Hello, world. You're at the function view")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the class view")


def year_post(request, year):
    text = ""
    ...  # Формируем статьи за год
    return HttpResponse(f'Post from {year}<br>{text}')


class MonthPost(View):
    def get(self, request, year, month):
        text = ''
        ...  # Формируем статьи за год и месяц
        return HttpResponse(f'Post from {month}/{year}<br>{text}')


def post_detail(request, year, month, slug):
    ...  # Формируем статьи за год и месяц по идентификатору.
    # Пока обойдемся без запросов к базе данных.
    post = {
        'year': year,
        'month': month,
        'slug': slug,
        'title': "Кто быстрее создает списки в Python, list() или []?",
        'content': "В процессе написания очередной программы, задумался над тем, "
                   "какой способ создания списков в Python работает быстрее...",
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {'name': 'Sweetslav'}
    return render(request, 'myapp3/my_template.html', context)


class TempleIf(TemplateView):
    template_name = 'myapp3/temple_if.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello World!'
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict':my_dict}
    return render(request, 'myapp3/temple_for.html', context)


def index(request):
    return render(request, 'myapp3/index.html')


def about(request):
    return render(request, 'myapp3/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post})
