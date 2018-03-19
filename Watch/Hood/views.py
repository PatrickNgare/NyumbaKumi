from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User_profile,Post,Neigbourhood,Business
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
            
            return redirect('post')
            messages.success(request, 'Status  updated '\
                                      'successfully')
        else:
            form = UploadForm()
    return render(request,'temps/upload.html',{"title":title, "user":current_user,"form":form})

@login_required(login_url='/accounts/login/')    
def post(request):
    current_user = request.user
    update= Post.objects.all()
    return render(request,'temps/post.html',{"update":update,"user":current_user})
  

def group(request):
    
    group=Neigbourhood.objects.all()

    return render(request,'temps/group.html',{'group':group})  



def allbiz(request):
    business=Business.objects.all()

    return render(request,'temps/allbiz.html',{"business":business})    