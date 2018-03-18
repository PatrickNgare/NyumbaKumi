from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User_profile,Post
from django.contrib.auth.decorators import login_required
from .forms import UploadForm

@login_required(login_url='/accounts/login/') 
def index(request):
    
    update= Post.objects.all()

    return render(request,'temps/index.html',{"update":update})
    
  
@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    title = 'Mtaa | Upload'
    profiles = User_profile.get_profile()
    for profile in profiles:
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.profile = profile
            upload.save()
            
            return redirect('index')
            messages.success(request, 'Status  updated '\
                                      'successfully')
        else:
            form = UploadForm()
    return render(request,'temps/upload.html',{"title":title, "user":current_user,"form":form})
     
def post(request):

    update= Post.objects.all()
    return render(request,'temps/post.html',{"update":update})
