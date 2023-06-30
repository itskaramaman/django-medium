from django.db import models
from django.contrib.auth.models import User
from app.models import BaseModel


class AppUser(BaseModel, User):
    website = models.CharField(null=True, blank=True)
