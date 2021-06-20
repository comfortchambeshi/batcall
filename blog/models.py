from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, default='null')
    category = models.CharField(max_length=250, default='null')
    slug = models.SlugField()
    body = RichTextUploadingField()
    published_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.png', blank=True)
    
    
    def __str__(self):
      return self.title
