from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name="blog-list"),
    path('<id>/', views.blog_details, name="blog-details")
]
