from django.urls import path
from . import views

urlpatterns = [
    #path for categories
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_categories, name='add_categories'),
    path('categories/edit/<int:pk>',views.edit_categories, name='edit_categories'),
    path('categories/delete/<int:pk>',views.delete_categories, name='delete_categories'),
    
    #path for [post]
    path('posts/', views.posts, name="posts"),
    path('posts/delete/<int:pk>',views.delete_posts,name='delete_posts'),
    ]

