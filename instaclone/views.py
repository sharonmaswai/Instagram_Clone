from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
            profile.username = current_user
            profile.user_id=current_user.id
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'create-profile.html', {"form":form})
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    posts=Image.objects.filter(profile_id=current_user.id)
    return render(request, 'profile.html',{"profile":profile,"posts":posts})