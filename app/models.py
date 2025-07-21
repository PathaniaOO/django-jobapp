from django.db import models
from django.utils.text import slugify

class Skill(models.Model):
    name = models.CharField(max_length=200)
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    company= models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

class Location(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=200)

# Create your models here.
class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
        ('Temporary', 'Temporary'),
        ('Volunteer', 'Volunteer'),
        ('Remote', 'Remote'),
        ('On-site', 'On-site'),
    ]
    CURRENCY_CHOICES=[
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('INR', 'Indian Rupee'),
        ('GBP', 'British Pound'),
        ('JPY', 'Japanese Yen'),
    ]
    title=models.CharField(max_length=100)
    description = models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    expiry_date=models.DateTimeField(null=True)
    salary=models.IntegerField()
    slug=models.SlugField(null=True,max_length=40, unique=True)
    Location=models.OneToOneField('Location', on_delete=models.CASCADE, null=True, blank=True)
    author=models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)
    skill=models.ManyToManyField('Skill', blank=True)
    type=models.CharField(max_length=100,null=False,choices=JOB_TYPE_CHOICES)
    currency=models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} with salary {self.salary}"
    


    # def __str__(self):
    #     return f"{self.city}, {self.state}, {self.country} for {self.job.title}"
