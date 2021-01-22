from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
## For better look ups in search:
from django.db.models import Q


class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        # print method_dict
        query = method_dict.get('q', None)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
        '''
        __icontains = field contains the query thing
        __iexact = fields is exactly as the query
        '''
