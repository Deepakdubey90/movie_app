from django.contrib import admin
from movie_category.models import (
    Movie,
    Category
)

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, AuthorAdmin)
admin.site.register(Category, AuthorAdmin)
