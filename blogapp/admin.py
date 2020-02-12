from django.contrib import admin
from .models import Post



# Register your models here.


#To register the Table named Post on your dashboard pass Post as an argument in the command admin.site.register()
admin.site.register(Post)