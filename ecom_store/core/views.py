from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class CheckOutView(TemplateView):
    template_name = "checkout.html"


class ProductView(TemplateView):
    template_name = "product.html"


class StoreView(TemplateView):
    template_name = "store.html"
