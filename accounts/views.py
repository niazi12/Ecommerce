from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.contrib.auth.forms import UserCreationForm
from django import forms
#from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import GuestForm
from .models import GuestEmail
#from django.contrib.auth.models import User
# Create your views here.

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/account/signup/")
    return redirect("/account/signup/")

# class SignUpView(generic.CreateView):
#     from_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


# class SignUpView(generic.CreateView):
#     model = User
#     fields = UserCreationForm.Meta.fields
#     from_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
