import datetime

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .utils import *


def home(request):
    featured_post = Posts.objects.get(id=1)
    posts_2_to_5 = Posts.objects.exclude(id=1)[:4]
    posts_6_to_last = Posts.objects.all()[5:Posts.objects.all().count()]

    for p in Posts.objects.all():
        p.com_count = p.comments_set.all().count()
        p.save()

    context = {
        'category': category,
        'posts_2_to_5': posts_2_to_5,
        'featured_post': featured_post,
        'latest_posts': latest_posts,
        'latest_comments': latest_comments,
        'posts_6_to_last': posts_6_to_last,
    }
    return render(request, 'main_page.html', context=context)


def get_category_count(cat_name):
    count = 0
    for cat in Posts.objects.values('category__title'):
        if cat['category__title'] == cat_name:
            count += 1
    return count


def characters(request):
    return render(request, 'characters.html')


def game(request):
    return render(request, 'game.html')


def category_view(request, cat_slug):
    c = Category.objects.get(slug=cat_slug)
    posts = Posts.objects.filter(category=c.id)

    context = {
        'latest_comments': latest_comments,
        'latest_posts': latest_posts,
        'category': category,
        'posts': posts,
    }

    return render(request, 'category.html', context=context)


def news(request):
    context = {
        'latest_comments': latest_comments,
        'category': category,
    }

    return render(request, 'news.html', context=context)


def single_post(request, post_slug):
    post = Posts.objects.get(slug=post_slug)
    comments = Comments.objects.filter(post_id=post.id)

    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form.cleaned_data['time_create'] = datetime.datetime.today()
            comment = form.save(commit=False)
            comment.author_id = request.user.id
            comment.post_id = post.id
            comment.save()
            return redirect(post.get_absolute_url())
    else:
        form = AddCommentForm()

    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'latest_comments': latest_comments,
        'latest_posts': latest_posts,
        'category': category,
    }
    return render(request, 'single-post.html', context=context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def create_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.cleaned_data['time_create'] = datetime.datetime.today()
                post = form.save(commit=False)
                post.author_id = request.user.id
                post.save()
                return redirect('home')
            except Exception as ex:
                print(ex)
    else:
        form = AddPost()

    return render(request, 'create_post.html', {'form': form})
