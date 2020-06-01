from django.shortcuts import render,redirect
from .models import Post,Profile,Like
from .forms import NewPostForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user)

        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()  

    context = {
        'u_form' :u_form,
        'p_form' :p_form
    }       

    return render(request,'all-info/profile.html', context) 

def show_post(request):
    posts = Post.objects.all()
    user = request.user

    context = {
        "post":posts,
        "user" : user
    }
    return render(request,'all-info/display.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'all-info/display.html'
    context_object_name = 'post'

class PostDetailView(DetailView):
    model = Post
    template_name = 'all-info/post_detail.html'
    
    


# def like_post(request, pk):
#     post = get_object_or_404(Post, id = request.POST.get('post_id'))
#     post.image_likes.add(request.user)
#     return HttpResponseRedirect(reverse('show_post', args=[str(pk)]))

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id = post_id)

        if user in post_obj.image_likes.all():
            post_obj.image_likes.remove(user)
        else:
            post_obj.image_likes.add(user) 

    like, created = Like.objects.get_or_create(user = user,post_id = post_id)

    if not created:
            if like.value == 'like':
                like.value = 'unlike'
            else :
                like.value = 'like'
            like.save()
    return redirect('show_post')        

    

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

def show_my_post(request):
    current_user = request.user
    post = get_object_or_404(Post.objects.all())
    profile = post.current_user

    context = {
        "profile" : profile
    }
    return render(request,'all-info/profile.html', context) 

def search_results(request):

    if 'post_profile' in request.GET and request.GET["post_profile"]:
        search_term = request.GET.get("post_profile")
        searched_users = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'all-info/search.html',{"message":message,"profiles": searched_users})

    else:
        message = "You haven't searched for any user"
        return render(request, 'all-info/search.html',{"message":message})    
        
