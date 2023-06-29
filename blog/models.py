from django.db import models
from django.contrib.auth.models import User
from app.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title[:10]


class Product(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title[:10]
