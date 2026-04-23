from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:id>/', views.delete_blog, name='delete_blog'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
]