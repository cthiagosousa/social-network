from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'created_at', 'updated_at', 'author')

admin.site.register(Account, UserAdmin)
admin.site.register(Post, PostAdmin)
