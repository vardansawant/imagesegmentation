from django.urls import path, include
import app.views as views

urlpatterns = [
    path('', views.index),
]

