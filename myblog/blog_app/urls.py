from os import name
from django.urls import path, include
from django.views import View
from blog_app import views

#app_name = 'blog_app'

urlpatterns = [
    path('', views.PostListView.as_view(), name = 'postList'),
    
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'detail_post'),
    path('post/new/', views.CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/edit', views.UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/remove/', views.DeletePostView.as_view(), name='delete_post'), 
    path('draft/', views.draftListView.as_view(), name='drafts'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='approve_comment'),
    path('comment/<int:pk>/delete/', views.comment_delete_view, name='delete_comment'),
    path('post/<int:pk>/publish/', views.post_publish_view, name='post_publish')
    




]
