from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('characters/', characters, name='characters'),
    path('game/', game, name='game'),
    path('category/<slug:cat_slug>', category_view, name='category'),
    path('news/', news, name='news'),
    path('post/<slug:post_slug>/', single_post, name='post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_post/', create_post, name='create_post'),
]
