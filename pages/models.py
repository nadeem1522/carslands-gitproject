from django.db import models

# Create your models here.

class Teams(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    desgin =models.CharField(max_length=150)
    photo = models.ImageField( upload_to='photos/%Y/%m/%d')
    facebook_link = models.URLField(max_length=200)
    twitter_link =models.URLField(max_length=200)
    Google_Plus_link= models.URLField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    