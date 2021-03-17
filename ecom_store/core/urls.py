from django.urls import path
from .views import IndexView, CheckOutView, ProductView, StoreView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('checkout/', CheckOutView.as_view(), name="checkout"),
    path('product/', ProductView.as_view(), name="product"),
    path('store/', StoreView.as_view(), name="store")
]