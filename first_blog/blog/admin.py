from django.contrib import admin

from .models import Author, Post


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ('pk', 'name', 'country')
    list_display_links = ('pk', 'name', 'country')

    fieldsets = (
        (None, {
            'fields': ('name', 'image', 'background_image', 'about_text', 'country',
                       'email', 'twitter_share', 'facebook_share', 'google_plus_share')
        }),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('pk', 'title', 'author', 'last_edit_date', 'create_post_date')
    list_display_links = ('pk', 'title', 'author')
    fieldsets = (
        (None, {
            'fields': ('title', 'prew', 'image_prew', 'author')
        }),
    )



