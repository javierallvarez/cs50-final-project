from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'time')
    
class NewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'content', 'image')

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Topic)
