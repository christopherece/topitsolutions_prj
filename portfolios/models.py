from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title