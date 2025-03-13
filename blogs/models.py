from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    content = models.TextField()  # Full content of the blog post
    author = models.CharField(max_length=100)  # Author of the blog post
    created_at = models.DateTimeField(default=timezone.now)  # Time the blog post was created
    updated_at = models.DateTimeField(auto_now=True)  # Time the blog post was last updated
    published_at = models.DateTimeField(null=True, blank=True)  # Optional field for when the post is published
    slug = models.SlugField(unique=True)  # Slug for SEO-friendly URLs

    # Image field to upload an image for each blog post
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Store image in 'blog_images/' folder

    # Optionally, you can add categories or tags if you want
    CATEGORY_CHOICES = [
        ('WEB_DEV', 'Web Development'),
        ('ICT_SUPPORT', 'ICT Support'),
        ('TECH_TIPS', 'Tech Tips'),
        ('MAINTENANCE', 'Maintenance'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='WEB_DEV'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # To redirect to the blog post detail page after saving
        return f"/blog/{self.slug}/"

    class Meta:
        ordering = ['-created_at']  # Display the newest posts first
