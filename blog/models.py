from django.db import models
from accounts.models import Profile
from django.utils.translation import gettext_lazy as _
from datetime import datetime
# Create your models here.
from django.utils.text import slugify

class blog(models.Model):
    user=models.ForeignKey(Profile,blank=True, null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    text=models.TextField(max_length=10000)
    img=models.ImageField(upload_to='blog/')
    catergryy=models.ManyToManyField('catergry',blank=True, null=True)
    
    views=models.IntegerField(default=0)

    likes=models.ManyToManyField(Profile,blank=True, null=True, related_name='liked_posts')
    count_likes=models.IntegerField(default=0)

    Created_At=models.DateTimeField(verbose_name=_("Created At"), default=datetime.now)
    
    slug=models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        else:
            self.slug = self.slug
        super(blog, self).save(*args, **kwargs)


class catergry(models.Model):
    title=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title 


class Comments(models.Model):
    user=models.ForeignKey(Profile,blank=True, null=True,on_delete=models.CASCADE)
    blog=models.ForeignKey(blog,blank=True, null=True,on_delete=models.CASCADE)
    comment=models.CharField(max_length=500)
    Created_At=models.DateTimeField(verbose_name=_("Created At"), default=datetime.now)
    
    def __str__(self):
        return str(self.user)