from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import (
    BlogPostSerializer,
    ProjectCategorySerializer,
    ProjectListSerializer,
    ProjectDetailSerializer,
    ContactUsSerializer
)
from core.models import BlogPost, ProjectCategory, Project, ContactUs
# Create your views here.

class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'id'

class ProjectCategoryListView(ListAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer

class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer

class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = 'id'


class ContactUsCreateView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        return serializer.save()