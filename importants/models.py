from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class important(models.Model):
    CATEGORIES = (
        ('privacy_policy', 'privacy_policy'),
       ('tos','tos'),
       ('cookie_policy', 'cookie_policy'),
       ('refund_policy', 'refund_policy'),
       ('licence', 'licence'),
       ('about_us', 'about_us'),
       ('aim', 'aim'),
    )
    title = models.CharField(max_length=250)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    main_body = RichTextUploadingField()
    category = models.CharField(max_length=250, choices=CATEGORIES, default='', unique=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return self.title





    
    
