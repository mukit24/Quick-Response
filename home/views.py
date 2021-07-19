from django.shortcuts import render,redirect
from .forms import ProfileForm,UpdateProfileForm,UserForm
from .models import Profile
from problems.models import Problem, Solution
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def home_view(request):
    print('yoo')
    context = {

    }
    return render(request,"home/home.html",context)


def profile_view(request,id,msg=None):
    form = ProfileForm()
    user = User.objects.get(id=id)
    print(user)
    alert = ''
    if msg == 'required':
        alert = 'You Must Create A Profile First'
    try:
        profile = Profile.objects.get(user=user)
        update_form = ProfileForm(instance=profile)
        pass_form = PasswordChangeForm(user=user)
        solved = Problem.objects.filter(Q(author=profile.user) & Q(is_solved=True)).count()
        unsolved = Problem.objects.filter(Q(author=profile.user) & Q(is_solved=False)).count()
    except:
        profile = ''
        update_form = ''
        pass_form = ''
        solved = ''
        unsolved = ''
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
        'user':user,
        'profile': profile,
        'update_form':update_form,
        'pass_form':pass_form,
        'solved_count':solved,
        'unsolved_count':unsolved,
        'alert':alert,
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


def points_table(request):
    profiles = Profile.objects.all().order_by('-total_points')
    context = {
        'profiles':profiles,
    }
    return render(request,'home/points.html',context)
            