from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'image', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comment', 'post', 'created_on', 'is_show')
    list_filter = ('is_show', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['reject_comments', 'accept_comments']

    def reject_comments(self, request, queryset):
        queryset.update(is_show=False)

    def accept_comments(self, request, queryset):
        queryset.update(is_show=True)


admin.site.register(Comment, CommentAdmin)
