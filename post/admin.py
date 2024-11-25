from django.contrib import admin
from .models import CustomUser , Post , Comment , Message


class CustomUserAdmin(admin.ModelAdmin):
    listDisplay = ['username', 'email', 'password']


admin.site.register(CustomUser, CustomUserAdmin)


class PostAdmin(admin.ModelAdmin):
    listDisplay = ['author', 'text' , 'image' , 'video']


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    listDisplay = ['author', 'post', 'text']


admin.site.register(Comment, CommentAdmin)


"""
class LikeAdmin(admin.ModelAdmin):
    listDisplay = ['author', 'post']


admin.site.register(Like, LikeAdmin)


class DisLikeAdmin(admin.ModelAdmin):
    listDisplay = ['author', 'post']


admin.site.register(DisLike, DisLikeAdmin)
"""

class MessageAdmin(admin.ModelAdmin):
    listDisplay = ['sender', 'recipient', 'content', 'timestamp']


admin.site.register(Message, MessageAdmin)