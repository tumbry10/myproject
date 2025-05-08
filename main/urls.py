from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('book_details/<int:id>/', views.book_details, name='book_details'),
    path('user_feedback', views.user_feedback, name='user_feedback'),
]