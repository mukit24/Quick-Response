from django.shortcuts import render,redirect
from .forms import PostForm,SolutionForm,CommentForm
from django.http import JsonResponse
from .models import Problem, Solution,Tag,Comment
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


def create_problem(request):
    if not request.user.is_authenticated:
        print('yooooooooo')
        return JsonResponse({'status':'fail'})
    if request.method == "POST":
        post_form = PostForm(request.POST)
        print(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            post_form.save_m2m()
            tags = []
            print(new_post.created_on)
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
            # return redirect('prob_home')
        else:
            print(post_form.errors)
            return JsonResponse(dict(post_form.errors.items()))

def delete_problem(request,id):
    problem = Problem.objects.get(id=id)
    problem.delete()
    return redirect('prob_home')

def edit_problem(request,id):
    problem = Problem.objects.get(id=id)
    form = PostForm(request.POST or None,instance=problem)
    if form.is_valid():
        form.save()

def problem_details(request,id,msg=None):
    print(msg)
    problem = Problem.objects.get(id=id)
    solutions = Solution.objects.filter(problem=problem)
    sol_cnt = Solution.objects.filter(problem=problem).count()
    sol_form = SolutionForm()
    cmt_form = CommentForm()
    update_post_form = PostForm(request.POST or None,instance=problem)

    success=''
    error=''

    if msg == 'success':
        success = 'Solution Is Successfully Added'
    elif msg == 'error':
        error = 'Error! Solution Can\'t be Blank'
    else:
        pass
    
    context = {
        'problem':problem,
        'sol_form':sol_form,
        'cmt_form':cmt_form,
        'solutions':solutions,
        'total_sol':sol_cnt,
        'success':success,
        'error': error,
        'update_post_form':update_post_form,

    }
    return render(request,"problems/problem_details.html",context)


def comment(request,id):
    if not request.user.is_authenticated:
        return JsonResponse({'status':'fail'})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if request.resolver_match.url_name == 'comment_problem':
            problem = Problem.objects.get(id=id)
            if form.is_valid():
                new_cmt = form.save(commit=False)
                new_cmt.author = request.user
                new_cmt.problem = problem
                new_cmt.save()
                form.save_m2m()

                data = {
                'id':new_cmt.id,
                'c_body':new_cmt.c_body,
                'author':new_cmt.author.username,
                'date':new_cmt.created_on,
                }
                return JsonResponse({'comment_data':data,'status':'success'})
            else:
                # print(form.errors)
                print('yoo')
                return JsonResponse({})


def delete_comment(request):
    id = request.GET['sid']
    cmt = Comment.objects.get(id=id)
    cmt.delete()
    return JsonResponse({'status':'success'})


def edit_comment(request):
    if request.method == 'POST':
        # print(request.POST)
        id = request.POST['cmt_id']
        cmt = Comment.objects.get(id=id)
        form = CommentForm(request.POST,instance=cmt)
        if form.is_valid():
            form.save()

            data = {
            'id':cmt.id,
            'c_body':cmt.c_body,
            'author':cmt.author.username,
            'date':cmt.created_on,
            }
            return JsonResponse({'edit_data':data,'status':'success'})
        else:
            return JsonResponse({})

@login_required
def create_solution(request,id):
    problem = Problem.objects.get(id=id)
    if request.method == "POST":
        sol_form = SolutionForm(request.POST)
        print(request.POST)
        if sol_form.is_valid():
            new_sol = sol_form.save(commit=False)
            new_sol.author = request.user
            new_sol.problem = problem
            new_sol.save()
            sol_form.save_m2m()
            return redirect('problem_details',problem.id,'success')
        else:
            return redirect('problem_details',problem.id,'error')
    else:
        return redirect('problem_details',problem.id)

def edit_solution(request,id):
    pass

