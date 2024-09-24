from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
    
class Location(models.Model):
    Mkoa = models.CharField(max_length=100)
    Wilaya = models.CharField(max_length=100)
    Jamii = models.CharField(max_length=100)
    Mtaa = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Mkoa}, {self.Wilaya}, {self.Jamii}, {self.Mtaa}"