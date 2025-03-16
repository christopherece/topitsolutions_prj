from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/')
    description = RichTextField(blank=True)
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)  # Time the blog post was created

    def __str__(self):
        return self.title