from django.urls import path, re_path
from . import views

urlpatterns = [
    # The home page
    path('', views.index, name='dashboard'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),


    # attributes
    path('attributes/', views.AttributesListView.as_view(), name="attributes-list"),
    path('attributes/new/', views.AttributeCreateview.as_view(), name="new-attribute"),
    path('attributes/<pk>/delete/', views.AttributeDeleteView.as_view(), name="delete-attribute"),
    path('attributes/<pk>/edit/', views.AttributeUpdateView.as_view(), name="update-attribute")
]
