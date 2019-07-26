from django.urls import path

from . import views # loads the views in the current package before others

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
]