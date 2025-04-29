from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_details/<int:id>/', views.book_details, name='book_details'),
    path('user_feedback', views.user_feedback, name='user_feedback'),
]