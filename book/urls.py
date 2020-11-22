from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from .views import LikeView, DisLikeView

urlpatterns = [
    path('', views.home, name="book-home"),
    path('about/', views.about, name="book-about"),
    path('booksearch/', views.booksearch, name = "booksearch"),
    path('books/', views.books, name = "books"),
    path('books/children', views.children, name = "children"),
    path('books/teen', views.teen, name = "teen"),
    path('like/<int:pk>', LikeView, name = "like_book"),
    path('dislike/<int:pk>', DisLikeView, name = "dislike_book"),
    path('policy', views.policy, name = "policy")
]
