from django.urls import path,include
from .views import prob_home,create_problem,problem_details,comment,delete_comment,edit_comment,create_solution,delete_problem,edit_problem,upvote,downvote,best_answer
urlpatterns = [
    path('',prob_home,name='prob_home'),
    path('create/',create_problem,name='create_problem'),
    path('<int:id>/details/',problem_details,name='problem_details'),
    path('<int:id>/details/<str:msg>/',problem_details,name='problem_details'),
    path('oldest/',prob_home,name='sort_oldest'),
    path('unsolved/',prob_home,name='sort_unsolved'),
    path('solved/',prob_home,name='sort_solved'),
    path('tag/',prob_home,name='sort_tag'),
    path('<int:id>/comment_problem/',comment,name='comment_problem'),
    path('delete_comment/',delete_comment,name='delete_comment'),
    path('edit_comment_problem/',edit_comment,name='edit_comment_problem'),
    path('create_solution/<int:id>/',create_solution,name='create_solution'),
    path('<int:id>/delete_problem/',delete_problem,name='delete_problem'),
    path('<int:id>/edit_problem',edit_problem,name='edit_problem'),
    # path('<int:id>/delete',delete_solution,name='delete_solution'),
    path('upvote/',upvote,name='upvote'),
    path('downvote/',downvote,name='downvote'),
    path('best_answer/',best_answer,name='best_answer'),
    path('<int:id>/profile/problems',prob_home,name='profile_view_problems'),
]
