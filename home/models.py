from django.db import models

# Create your models here.
class Collections (models.Model):
    name = models.CharField(max_length=50)
    caption = models.TextField()
    img = models.ImageField(upload_to='pics')
    
class Workings (models.Model):
    name = models.CharField(max_length=50)
    caption = models.TextField()
    img = models.ImageField(upload_to='pics')

class Buying (models.Model):
    name = models.CharField(max_length=50)
    order_description = models.TextField()
    phone_number = models.TextField()
    username=models.CharField(max_length=100)

class Image (models.Model):
    img=models.ImageField(upload_to='images')


class Feed(models.Model): 
    caption = models.CharField(max_length=50) 
    post_img = models.ImageField(upload_to='posts') 
    username = models.CharField(max_length=50) 












# class Post (models.Model):
#     img=models.ImageField(upload_to='posts')
#     caption=models.TextField()

# # class Postnewsfeed (models.Model):
# #     img=models.ImageField(upload_to='posts')
# #     caption=models.TextField()