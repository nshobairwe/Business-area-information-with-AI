from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='location_images/')
    # Add other fields as needed
    class Meta:
        db_table = "Area"  # Set the table name explicitly
    def __str__(self):
        return self.description
