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
    path('attributes/<pk>/edit/', views.AttributeUpdateView.as_view(), name="update-attribute"),

    # categories
    path('categories/', views.CategoriesListView.as_view(), name="categories-list"),
    path('categories/new/', views.CategoryCreateview.as_view(), name="new-category"),
    path('categories/<pk>/delete/', views.CategoryDeleteView.as_view(), name="delete-category"),
    path('categories/<pk>/edit/', views.CategoryUpdateView.as_view(), name="update-category"),
    path('categories/<pk>', views.CategoryDetailView.as_view(), name="category-detail"),

    # products
    path('products/', views.IProductLIstview.as_view(), name="product-list"),
    path('products/new/', views.IProductCreateview.as_view(), name="new-product"),
    path('products/<pk>/delete/', views.IProductDeleteView.as_view(), name="delete-product"),
    path('products/<pk>/edit/', views.IProductUpdateView.as_view(), name="update-product"),
    path('products/<pk>', views.IProductDetailView.as_view(), name="product-detail")

]
