from django.shortcuts import render,redirect
from .forms import ProfileForm,UpdateProfileForm,UserForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
# Create your views here.
def home_view(request):
    print('yoo')
    context = {

    }
    return render(request,"home/home.html",context)


def profile_view(request,id):
    form = ProfileForm()
    user = User.objects.get(id=id)
    print(user)
    try:
        profile = Profile.objects.get(user=user)
        update_form = ProfileForm(instance=profile)
        pass_form = PasswordChangeForm(user=user)
    except:
        profile = ''
        update_form = ''
        pass_form = ''
    # print(Profile.objects.get(user=user))

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            form.save_m2m()
            return redirect('profile_view',user.id)
    context = {
        'form':form,
        'profile': profile,
        'update_form':update_form,
        'pass_form':pass_form,
    }
    return render(request,"home/profile.html",context)


def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    form = ProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile_view', user.id)
    return redirect('profile_view', user.id)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            print('success') 
            return JsonResponse({'status':'success'})
        else:
            return JsonResponse(dict(form.errors.items()))
            