from django.contrib import admin
from .models import Collections
from .models import Workings,Buying,Image

# Register your models here.

admin.site.register(Collections)
admin.site.register(Workings)
admin.site.register(Buying)
admin.site.register(Image)