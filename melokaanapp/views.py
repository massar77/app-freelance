from django.shortcuts import render
from .models import Post, Category_1, Category_2
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    posts = Post.objects.all()
    categories_1 = Category_1.objects.all()
    categories_2 = Category_2.objects.all()

    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_objs = paginator.get_page(page_number)

    context = {
        'page_objs':page_objs,
        'categories_1':categories_1,
        'categories_2':categories_2,
    }
    return render(request, 'home.html', context)


def post(request, slug_text):
    post = Post.objects.get(slug=slug_text)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context)


def categorie(request, slug_text):
    posts = Category_1.objects.filter(slug=slug_text)
    context = {
        'posts': posts,
    }
    return render(request, 'categorie.html', context)


def sous_categorie(request, slug_text):
    posts = Category_2.objects.filter(slug=slug_text)
    context = {
        'posts': posts,
    }
    print(posts)
    return render(request, 'sous_categorie.html', context)