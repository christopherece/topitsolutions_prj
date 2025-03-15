from django.contrib import admin
from . models import ContactMessage, Testimonial
# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company')
    search_fields = ('name', 'position', 'company')


admin.site.register(Testimonial, TestimonialAdmin)