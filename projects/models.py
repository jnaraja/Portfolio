from django.db import models

# Create your models here.
class Project(models.Model):
    # Images
    image = models.ImageField(upload_to='images/')
    # Summary character count
    summary = models.CharField(max_length=200)