from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment, Instalikes
from django.contrib.auth.models import User


from .forms import ProfileForm, PostForm, CommentForm

def index(request):

    return render(request, 'display/index.html')

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            # profile.username = current_user
            profile.user_id=current_user.id
            profile.save()
    
        return redirect('profile')
    else:
        form = ProfileForm()
    
    return render(request, 'create-profile.html', {"form":form})
def profile(request):
    
    current_user = request.user
    profile = Profile.objects.get(name=current_user)
    posts=Image.objects.filter(profile_id=current_user.id)
    return render(request, 'profile.html',{"profile":profile, 'posts':posts})
def home(request):
    current_user = request.user
    posts = Image.objects.all()
    users = Profile.objects.all()
    
    comments = Comment.objects.all()
    #likes = Instalikes.objects.all
    profile = Profile.objects.all()
   
    
    return render(request, 'home.html', {"posts":posts, 'users':users, 'comments':comments ,'profile':profile})
def comment(request, image_id):

    current_user = request.user
    
    image = Image.objects.get(id=image_id)
    owner = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user_comment = current_user
            comment.save()

            # print(comments)


        return redirect('home')
    else:
        form = CommentForm()

    return render(request, 'create-comment.html', {"form": form,'image_id':image_id, 'comments':comments}, locals())
def likes(request, image_id):
    current_user = request.user
    post=Image.objects.get(id=image_id)
    like_pic,created= Instalikes.objects.get_or_create(instalikes=current_user, post=post)
    like_pic.save()

    return redirect('home')


@login_required(login_url='accounts/login/')    
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.save()
        return redirect('home')

    else:
        form = PostForm()
    return render(request, 'new-post.html', {"form": form})