from django.shortcuts import render,redirect
from .forms import PostForm
from django.http import JsonResponse
from .models import Problem
# Create your views here.
def prob_home(request):
    post_form = PostForm()
    problems = Problem.objects.all().order_by('-created_on')
    context = {
        'post_form':post_form,
        'problems':problems,
    }
    return render(request,"problems/index.html",context)

def create_problem(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            post_form.save_m2m()
            return redirect('prob_home') 
        else:
            return redirect('prob_home')