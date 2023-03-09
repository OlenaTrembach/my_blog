from .models import Post, Comments
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)


# Register your models here.
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author')
#

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'text_comment')
