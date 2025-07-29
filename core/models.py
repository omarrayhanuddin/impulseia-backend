from django.db import models


# Create your models here.
class BlogPost(models.Model):
    thumbnail = models.ImageField(upload_to="blog_thumbnails/", blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"


# this model represent project for portfolio
class Project(models.Model):
    thumbnail = models.ImageField(
        upload_to="project_thumbnails/", blank=True, null=True
    )
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        ProjectCategory, on_delete=models.SET_NULL, null=True, related_name="projects"
    )
    description = models.TextField()
    web_url = models.URLField(blank=True, null=True)
    playstore_url = models.URLField(blank=True, null=True)
    appstore_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="project_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.project.name}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Us Message"
        verbose_name_plural = "Contact Us Messages"
