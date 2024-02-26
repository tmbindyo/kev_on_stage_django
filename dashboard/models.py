import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import Group, GroupManager, PermissionsMixin

from .managers import UserManager

# Create your models here.
from .mixins import (
    DeletionMarkerMixin,
    HistoricalDataMixin,
    TimestampMixin,
)    

    
class Tour(DeletionMarkerMixin, HistoricalDataMixin, TimestampMixin):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    clicks = models.IntegerField(default=0)
    is_sold_out = models.BooleanField(default=False)

    status_id = models.IntegerField()  # Adjust this field based on your specific requirements
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=False, null=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} @ {self.date} {self.time}'



class Status(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()

    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name