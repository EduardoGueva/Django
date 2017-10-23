#-*-coding:utf-8-*-

from django.contrib import admin

# Register your models here
from .models import Post

class PostAdmin(admin.ModelAdmin):
	ordering=('-id',)
	search_fields=('title','body',)
admin.site.register(Post,PostAdmin)