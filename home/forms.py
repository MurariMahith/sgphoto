from django import forms 
from .models import *
  
class FeedForm(forms.ModelForm): 
  
    class Meta: 
        model = Feed 
        fields = ['caption', 'post_img','username']




















# from django import forms
# from . import models
# from .models import Post

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.ImageField()



# class HotelForm(forms.ModelForm): 
  
#     class Meta: 
#         model = Post
#         fields = ['title', 'file'] 