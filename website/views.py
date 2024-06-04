from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm, NewsletterForm


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            new_contact = contact_form.save(commit=False)
            new_contact.name = "anonymous user"
            contact_form.save()
            messages.success(request, "your ticket submitted successfully")
        else:
            messages.error(request, "your ticket didn't submitted")

    contact_form = ContactForm()
    return render(request, 'website/contact.html', {'form': contact_form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            messages.success(request, "you are joined to our newsletter")
            form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "your email is invalid ")
    else:
        return HttpResponseRedirect('/')
