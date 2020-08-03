from django.urls import path
from .views import home_view, lookup_view

urlpatterns = [
    path('', home_view),
    path('lookup/<name>', lookup_view)
]
