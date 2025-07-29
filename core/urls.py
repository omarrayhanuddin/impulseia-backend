from django.urls import path
from core.views import (
    BlogPostListView,
    BlogPostDetailView,
    ProjectCategoryListView,
    ProjectListView,
    ProjectDetailView,
    ContactUsCreateView
)

urlpatterns = [
    path('blogs', BlogPostListView.as_view(), name='blog-list'),
    path('blog/<int:id>', BlogPostDetailView.as_view(), name='blog-detail'),
    path('categories', ProjectCategoryListView.as_view(), name='project-category-list'),
    path('projects', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:id>', ProjectDetailView.as_view(), name='project-detail'),
    path('contact/create', ContactUsCreateView.as_view(), name='contact-create'),
]
