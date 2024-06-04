from django import forms

from .models import Contact, Newsletter


class ContactForm(forms.ModelForm):
    subject = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
