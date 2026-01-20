from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline, name='timeline'),
    path('post_create', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('signup/', views.signup, name='signup'),
    path('api/posts/', views.api_posts, name='api_posts'),
]
