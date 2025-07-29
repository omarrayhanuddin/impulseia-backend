from rest_framework import serializers
from core.models import BlogPost, ProjectCategory, Project, ProjectImage, ContactUs


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id","thumbnail", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class ProjectSerializer(serializers.ModelSerializer):
    category = ProjectCategorySerializer(read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "category",
            "description",
            "url",
            "created_at",
            "updated_at",
            "images"
        ]
        read_only_fields = ["created_at", "updated_at"]


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ["id", "name", "email", "message", "created_at"]
        read_only_fields = ["created_at"]
