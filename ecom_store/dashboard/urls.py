from django.urls import path, re_path
from . import views

urlpatterns = [
    # The home page
    path('', views.index, name='dashboard'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
