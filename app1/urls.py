from django.urls import path
from . import views

urlpatterns = [
    path('v1app1/', views.v1_app1),
]