from django.contrib import admin
from unfold import admin as unfold_admin
from .models import BlogPost, ProjectCategory, Project, ProjectImage

# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(unfold_admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(unfold_admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("name",)


# project with inline images
class ProjectImageInline(unfold_admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ("image", "created_at")
    readonly_fields = ("created_at",)
    max_num = 10
    min_num = 1


@admin.register(Project)
class ProjectAdmin(unfold_admin.ModelAdmin):
    list_display = ("name", "category", "created_at", "updated_at")
    search_fields = ("name", "description")
    list_filter = ("category", "created_at")
    ordering = ("-created_at",)
    inlines = [ProjectImageInline]


@admin.register(ProjectImage)
class ProjectImageAdmin(unfold_admin.ModelAdmin):
    list_display = ("project", "image", "created_at")
    search_fields = ("project__name",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
