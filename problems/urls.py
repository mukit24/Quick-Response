from django.urls import path,include
from .views import prob_home,create_problem,problem_details
urlpatterns = [
    path('',prob_home,name='prob_home'),
    path('create/',create_problem,name='create_problem'),
    path('<int:id>/details/',problem_details,name='problem_details'),
    path('oldest/',prob_home,name='sort_oldest'),
    path('unsolved/',prob_home,name='sort_unsolved'),
    path('solved/',prob_home,name='sort_solved'),
    path('tag/',prob_home,name='sort_tag'),
]
