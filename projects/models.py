from django.db import models

# Create your models here.
class Project(models.Model):
    # Images
    image = models.ImageField(upload_to='images/')
    # Summary character count
    summary = models.CharField(max_length=200)
    # Link to project
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.summary