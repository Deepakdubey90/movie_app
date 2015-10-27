from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (AbstractUser)


class User(AbstractUser):
    deleted_on = models.DateTimeField(
        'Deleted On', null=True, blank=True, default=None, db_index=True)

    def __str__(self):
        return self.email if self.email else self.username

"""
class ProxyGroup(Group):

    class Meta:
        proxy = True
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
"""
