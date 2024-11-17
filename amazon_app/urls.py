from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('createauthor/', views.createAuthor, name='author'),
    path('add/', views.createBook, name='add_book'),
    path('about/', views.aboutUser, name='about'),
    path('contact/', views.contactUser, name='contact'),
    path('cart/', views.cartUser, name='cart'),
]