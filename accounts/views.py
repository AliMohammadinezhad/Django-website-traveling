from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            auth_form = AuthenticationForm(request=request, data=request.POST)
            if auth_form.is_valid():
                username = auth_form.cleaned_data.get('username')
                password = auth_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)                                    
                if user is not None: 
                    login(request, user)
                    return redirect('/')
        auth_form = AuthenticationForm()
        context = {'auth_form': auth_form}    
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')
        
            
        
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
        

def signup_view(request):
    pass
