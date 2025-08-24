from django.db import models


class Common(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, related_name="districts", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Setting(models.Model):
    phone = models.CharField(max_length=20)
    support_email = models.EmailField()
    working_hours = models.CharField(max_length=255)
    app_version = models.CharField(max_length=50)
    maintenance_mode = models.BooleanField(default=False)
