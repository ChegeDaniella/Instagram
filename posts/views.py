from django.shortcuts import render,redirect
from .models import Post,Profile
from .forms import NewPostForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    # user = Profile.objects.user
    # users = Profile.objects.filter(user = user).first()
    # user = Profile.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated')
            return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance = request.user.profile)  

        context = {
           'u_form' :u_form,
           'p_form' :p_form
       }       


    return render(request,'all-info/profile.html', context) 

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
