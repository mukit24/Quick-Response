from django.shortcuts import render,redirect
from .forms import PostForm
from django.http import JsonResponse
from .models import Problem,Tag
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.forms.models import model_to_dict

# Create your views here.
def prob_home(request):
    # print(request.resolver_match.url_name)
    post_form = PostForm()
    tags = Tag.objects.all().order_by('name')
    
    temp = Problem.objects.first()
    # tags = []
    # for x in temp.tag.all():
    #     tags.append(x.name)
    # data = {
    #     'name':temp.title,
    #     'tags':tags,
    # }
    # print(data)
    # print(model_to_dict(temp))
    # seri = {
    #     'title':temp.title,
    #     'author':temp.author.username,
    # }
    # print(seri)
    # a_seri = {
    #     'data':dict(temp),
    # }
    # print(a_seri)
    # print(seri['title'])

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
            tags = []
            for x in new_post.tag.all():
                tags.append(x.name)
            data = {
                'id':new_post.id,
                'title':new_post.title,
                'author':new_post.author.username,
                'is_solved':new_post.is_solved,
                'tags':tags,
                'date':new_post.created_on,
            }
            return JsonResponse({'problem_data':data,'status':'success'}) 
        else:
            print(post_form.errors)
            return JsonResponse(dict(post_form.errors.items()))


def problem_details(request,id):
    problem = Problem.objects.get(id=id)
    context = {
        'problem':problem,
    }
    return render(request,"problems/problem_details.html",context)








