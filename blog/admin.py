from django.contrib import admin
from .models import BlogPost
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['id','desc','user']

admin.site.register(BlogPost,PostAdmin)