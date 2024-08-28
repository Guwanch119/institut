from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from datetime  import datetime,date
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
            return self.name
    
    
    def get_absolute_url(self):
        #return reverse('engine:article-detail',args=(str(self.id)))
        return reverse('engine:tazelik')

    
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextUploadingField(blank = True, null = True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='tazelik')
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    
    def get_absolute_url(self):
        #return reverse('engine:article-detail',args=(str(self.id)))
        return reverse('engine:tazelik')
    
class Faculty(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True,null=True)
    
    
    def __str__(self):
        return self.title
    
    
        
        
    

