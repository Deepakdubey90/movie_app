from django.contrib import admin
from user.models import User


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, AuthorAdmin)
