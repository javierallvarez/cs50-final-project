from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.loginView, name="login"),
    path('logout', views.logoutView, name="logout"),
    path('register', views.register, name="register"),
    path('avatar', views.avatar, name="avatar"),
    path('news/<int:news_id>', views.single_news, name="single_news"),
    path("write_news", views.write_news, name="write_news"),
    path("readlist/", views.load_readlist, name="load_readlist"),
    path("add_to_readlist/", views.add_to_readlist, name="add_to_readlist"),

    # API routes:
    path("delete/", views.delete, name="delete"),
    path("edit/", views.edit_comment, name="edit"),
    path("post_comment/", views.post_comment, name="post_comment")
]