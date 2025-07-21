from django.db import models

# Create your models here
class Uploads(models.Model):
    file = models.ImageField(upload_to="images")
    description=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.description)
    
class Uploads2(models.Model):
    file = models.FileField(upload_to="files")
    description=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.description)

