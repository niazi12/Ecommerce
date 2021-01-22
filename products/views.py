from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from carts.models import Cart
from .models import Product


class ProductListView(ListView):
    #model = Product
    template_name = "products/list.html"
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        """
        We are oveerriding ListView's builtin method.
        This allows us to specify a query to show only the
        items that we want to show other than the default all
        that comes with model = product above
        """
        request = self.request
        return Product.objects.all()

class ProductDetailView(DetailView):
    #model = Product
    template_name = "products/detail.html"
    context_object_name = 'product' # or object can be used in template

    def get_object(self, *args, **kwargs):
        ''' Does same as query set '''
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        ''' Does same as query set '''
        request = self.request
        slug = self.kwargs.get('product_slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            return Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.object.filter(slug=slug, active=True)
            return qs.first()
        return instance
