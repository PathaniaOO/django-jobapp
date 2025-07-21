from django.db import models


NEWSLETTER_OPTION=[
    ('W','Weekly'),
    ('M','Monthly'),
    ('Q','Quarterly'),
]

# Create your models here.
class Subscribe(models.Model):
    firstname = models.CharField(max_length=100,blank=False,null=False)
    lastname = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(max_length=254,blank=False)
    option = models.CharField(max_length=2,choices=NEWSLETTER_OPTION,default='W')
    # date_subscribed = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.email

    # class Meta:
    #     verbose_name = 'Subscription'
    #     verbose_name_plural = 'Subscriptions'
    #     ordering = ['-date_subscribed']  # Orders by the most recent subscription first
