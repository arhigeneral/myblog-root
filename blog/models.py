from django.db import models

# Create your models here.

class Post(models.Model):
    blog_title = models.CharField(max_length =  30)
    blog_date = models.DateTimeField()
    blog_image = models.ImageField(upload_to = 'blog_images/')
    blog_text = models.TextField(max_length = 300)
