from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from .models import Userprofile

def signup(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)
            
            return redirect('/login/')
        
    else:
        form = UserChangeForm()
        
    form = UserChangeForm()
    
    return render(request, 'userprofile/signup.html', {
        'form': form
    })




