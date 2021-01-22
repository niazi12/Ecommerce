from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm
from products.models import Product

class HomePageView(TemplateView):
    title = "Home!"
    content = "Explore Our featured Items"
    featured_products = Product.objects.featured()
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['content'] = self.content
        context['featured_products'] = self.featured_products
        return context

class AboutPageView(TemplateView):
    title = "About"
    content = "Welcome to the about page"
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context.update({'title': self.title,
                        'content': self.content})
        return context

class ContactPageView(FormView):
    form_class = ContactForm
    title = "Contact"
    content = "Welcome to the contact page"
    template_name = 'contact/view.html'
    success_url = '/contact/'

    def form_valid(self, form):
        print(form.cleaned_data['email'])
        print(form.cleaned_data)
        return super(ContactPageView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        context.update({'title': self.title,
                        'content': self.content})
        return context
