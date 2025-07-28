from django.urls import path
from .views import KioskListView


urlpatterns = [
    path('kiosks/', KioskListView.as_view(), name='kiosks'),
]

