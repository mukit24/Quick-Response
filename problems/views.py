from django.shortcuts import render,redirect
from .forms import PostForm
from django.http import JsonResponse
from .models import Problem,Tag
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def prob_home(request):
    # print(request.resolver_match.url_name)
    post_form = PostForm()
    tags = Tag.objects.all().order_by('name')
    

    if request.resolver_match.url_name == 'sort_oldest':
        problems = Problem.objects.all().order_by('created_on')
    elif request.resolver_match.url_name == 'sort_unsolved':
        problems = Problem.objects.filter(is_solved=False).order_by('-created_on')
    elif request.resolver_match.url_name == 'sort_solved':
        problems = Problem.objects.filter(is_solved=True).order_by('-created_on')
    elif request.resolver_match.url_name == 'sort_tag':
        tag_list = request.POST.getlist('tag_choice')
        problems = Problem.objects.filter(tag__name__in=tag_list).order_by('-created_on').distinct()
    else:
        problems = Problem.objects.all().order_by('-created_on')

    paginator = Paginator(problems,10)
    page_number = request.GET.get('page')
    p_problems = paginator.get_page(page_number)

    context = {
        'post_form':post_form,
        'problems':p_problems,
        'tags':tags,
    }
    return render(request,"problems/index.html",context)


@login_required
def create_problem(request):
    if request.method == "POST":
        # print(request.POST)
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            post_form.save_m2m()
            return redirect('prob_home') 
        else:
            return redirect('prob_home')


def problem_details(request,id):
    problem = Problem.objects.get(id=id)
    context = {
        'problem':problem,
    }
    return render(request,"problems/problem_details.html",context)








