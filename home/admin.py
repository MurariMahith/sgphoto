from django.contrib import admin
from .models import Collections
from .models import *

# Register your models here.

admin.site.register(Collections)
admin.site.register(Workings)
admin.site.register(Buying)
admin.site.register(Image)
admin.site.register(Feed)



# admin.site.register(Post)
# admin.site.register(Postnewsfeed)
