from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class Category(models.Model):

    movie_type = models.CharField(
        _('Type'), max_length=16, db_index=True
    )
    value = models.CharField(
        _('Value'), max_length=30, db_index=True
    )

    def __str__(self):
        return self.movie_type


class Movie(models.Model):

    title = models.CharField(
        _('Title'), max_length=30, blank=False, null=True
    )
    description = models.CharField(
        _('Description'), max_length=30, blank=False, null=True
    )
    featured_image = models.ImageField(
        _('Featured image'), upload_to='images/%Y/%m/%d'
    )
    movie_length = models.CharField(
        _('Movie Length'), max_length=30, blank=False, null=True
    )
    movie_release_date = models.DateTimeField(
        _('Movie release date'), blank=True, default=None,
        null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('User'),
        null=True
    )
    category = models.ManyToManyField(Category, blank=True)

    deleted_on = models.DateTimeField(
        'Deleted On', null=True, blank=True, default=None
    )

    def __str__(self):
        return self.title
