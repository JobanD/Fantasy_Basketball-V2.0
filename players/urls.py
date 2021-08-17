from django.urls import path

from . import views

# Controls all urls contained within main app and which functions from views should be called appropriately

urlpatterns = [
    path('', views.players), # our-domain.com/main
]
