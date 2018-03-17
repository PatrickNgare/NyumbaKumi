from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import EditProfile

@login_required(login_url='/accounts/login/')
def index(request):
    

    return render(request,'temps/index.html')



def profile(request):
    
    
    return render(request,'temps/profile.html')




@login_required(login_url='/accounts/login/')
@transaction.atomic
def editprofile(request):
    if request.method == 'POST':
        profile_form = EditProfile(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('index')
    else:
        
        profile_form = EditProfile(instance=request.user)
    return render(request, 'temps/editprofile.html', {"profile_form": profile_form})    