from django.contrib import admin
from .models import Comment
from .models import Location

# myapp/admin.py

class LocationAdmin(admin.ModelAdmin):
    list_display = ('Mkoa', 'Wilaya', 'Jamii', 'Mtaa')  # Specify the columns you want to display in the list view
    search_fields = ('Mkoa', 'Wilaya', 'Jamii', 'Mtaa')  # Add fields to enable searching in the admin interface
    list_filter = ('Mkoa', 'Wilaya', 'Jamii')  # Add filters to narrow down the list view

# Register the Location model with the custom admin class
admin.site.register(Location, LocationAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message','timestamp')  # Specify the columns you want to display

# Register the Comment model with the custom admin class
admin.site.register(Comment, CommentAdmin)
