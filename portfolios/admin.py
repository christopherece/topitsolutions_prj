from django.contrib import admin
from .models import Portfolio
# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Fields to display in the list view
    search_fields = ('title',)  # Enable search by project title

# Register the Project model and its admin class
admin.site.register(Portfolio, PortfolioAdmin)
