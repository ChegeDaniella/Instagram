from django.shortcuts import render,redirect
from .models import Post
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'all-info/profile.html') 

def show_post(request):
    posts = Post.objects.all()
    return render(request,'all-info/display.html',{"post":posts})
    
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user   
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.image_profile = current_user
            post.save()
        return redirect('show_post')  
    else:
        form = NewPostForm()
        return render(request,'upload-page.html',{"form":form})          
