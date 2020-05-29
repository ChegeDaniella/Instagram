from django.shortcuts import render,redirect
from .models import Post
from .forms import NewPostForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'all-info/profile.html') 

def new_post(request):
    current_user = request.user   
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.image_profile = current_user
            post.save()
        return redirect('index')  
    else:
        form = NewPostForm()
        return render(request,'upload-page.html',{"form":form})          
