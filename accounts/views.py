from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import CustomUserCreationForm, CustomAuthenticationForm



class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('accounts:password_reset_done')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:password_reset_complete')
    

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            auth_form = CustomAuthenticationForm(request=request, data=request.POST)
            if auth_form.is_valid():
                user_input = auth_form.cleaned_data.get('username')
                password = auth_form.cleaned_data.get('password')
                remember_me = auth_form.cleaned_data.get('remember_me')
                user = authenticate(request, username=user_input, password=password)
                if user is not None:
                    login(request, user)
                    if remember_me: 
                    # This if statement can change, 
                    # but the purpose is checking remember me checkbox is checked or not.
                        request.session.set_expiry(604800) # Here we extend session.
                    else:
                        # This part of code means, close session when browser is closed.
                        request.session.set_expiry(0)
                    messages.success(request, "Login successful")
                    return redirect('/')
        auth_form = CustomAuthenticationForm()
        context = {'auth_form': auth_form}    
        return render(request, 'accounts/login.html', context)
    else: 
        return redirect('/')
        
            
        
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
        

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            signup_form = CustomUserCreationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, "you are Signed Up!")
                return redirect('accounts:login')

        signup_form = CustomUserCreationForm()
        context = {'form': signup_form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect("/")