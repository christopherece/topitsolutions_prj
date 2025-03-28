from django.db import models

# Create your models here.
from django.db import models

class ContactMessage(models.Model):
    website_url = models.URLField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/it_testimonials/')
    content = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.position} at {self.company}"



