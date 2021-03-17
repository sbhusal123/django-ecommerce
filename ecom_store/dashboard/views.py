from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from django import template

from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.shortcuts import reverse

from item.models import ProductAttributes, Category, Attributes, ProductImage, Product


@login_required(login_url="/login/")
def index(request):
    context = {
        'segment': 'index'
    }

    html_template = loader.get_template('dashboard/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template('dashboard/'+load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


class AttributesListView(ListView):
    template_name = 'dashboard/attributes/list_attribute.html'
    model = Attributes
    context_object_name = "attributes"
    paginate_by = 10


class AttributeCreateview(CreateView):
    template_name = 'dashboard/attributes/create_attributes.html'
    model = Attributes
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('attributes-list')


class AttributeDeleteView(DeleteView):
    model = Attributes

    def get_success_url(self):
        return reverse('attributes-list')


class AttributeUpdateView(UpdateView):
    model = Attributes
    fields = ['name', 'description']
    pk_url_kwarg = 'pk'
    template_name = 'dashboard/attributes/edit_attributes.html'

    def get_success_url(self):
        return reverse('attributes-list')


class CategoriesListView(ListView):
    template_name = 'dashboard/category/list_category.html'
    model = Category
    context_object_name = "categories"
    paginate_by = 10


class CategoryCreateview(CreateView):
    template_name = 'dashboard/category/create_category.html'
    model = Category
    fields = ['name', 'image', 'description']

    def get_success_url(self):
        return reverse('categories-list')



class CategoryDeleteView(DeleteView):
    model = Category

    def get_success_url(self):
        return reverse('categories-list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'image', 'description']
    pk_url_kwarg = 'pk'
    template_name = 'dashboard/category/edit_category.html'

    def get_success_url(self):
        return reverse('categories-list')


class CategoryDetailView(DetailView):
    model = Category
    pk_url_kwarg = 'pk'
    template_name = 'dashboard/category/category_detail.html'


class IProductLIstview(ListView):
    template_name = 'dashboard/inventory/list-product.html'
    model = Product


class IProductCreateview(CreateView):
    template_name = 'dashboard/inventory/add-product.html'
    model = Product
    fields = ['name', 'image', 'description']

    def get_success_url(self):
        return reverse('categories-list')


class IProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('categories-list')


class IProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'image', 'description']
    pk_url_kwarg = 'pk'
    template_name = 'dashboard/inventory/edit-product.html'

    def get_success_url(self):
        return reverse('categories-list')


class IProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = 'pk'
    template_name = 'dashboard/inventory/product-detail.html'
