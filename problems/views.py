from django.shortcuts import render
from .forms import PostForm
# Create your views here.
def prob_home(request):
    post_form = PostForm()
    context = {
        'post_form':post_form,
    }
    return render(request,"problems/index.html",context)