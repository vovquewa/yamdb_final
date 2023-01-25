from django.contrib import admin

from .models import User, Title, Genre, Categories, Review, Comment

admin.site.register(User)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'category')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class RewiewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pub_date', 'author', 'text', 'score', 'title')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Review, RewiewAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pub_date', 'author', 'text', 'review')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Comment, CommentAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Genre, GenreAdmin)
