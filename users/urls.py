from django.urls import path
from users import views

urlpatterns = [
    path('', views.user_list, name="user-list"),
    path('<int:id>/', views.user_details, name="user-details"),
    path('register/', views.register, name="register"),
]
