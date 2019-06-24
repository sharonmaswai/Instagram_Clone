from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile
from .forms import ProfileForm, PostForm
@login_required(login_url='/accounts/login/')
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
    # user = request.user
    # if request.method == "POST":
    #     form = ProfileForm(request.POST, request.FILES)
    #     if form.is_valid():
            
    #         profile =form.save(commit = False)
    #         profile.user = user
    #         profile.save()
            
    #         return redirect('profile')
    # else:
    #     form = ProfileForm()
    return render(request, 'create-profile.html', {"form":form})
def profile(request):
    
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    posts=Image.objects.filter(profile_id=current_user.id)
    return render(request, 'profile.html',{"profile":profile})
def home(request):
    current_user = request.user
    posts = Image.objects.all()
    print('-' * 30)
    for i in posts:
        print(i.image)
    # print(posts)
    # comments = Comment.objects.all()
    # likes = Likes.objects.all
    profile = Profile.objects.all()
    # print(likes)
    
    return render(request, 'home.html', {"posts":posts})

    
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