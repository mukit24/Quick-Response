from django.urls import path,include
from .views import prob_home,create_problem,problem_details,comment,delete_comment,edit_comment
urlpatterns = [
    path('',prob_home,name='prob_home'),
    path('create/',create_problem,name='create_problem'),
    path('<int:id>/details/',problem_details,name='problem_details'),
    path('oldest/',prob_home,name='sort_oldest'),
    path('unsolved/',prob_home,name='sort_unsolved'),
    path('solved/',prob_home,name='sort_solved'),
    path('tag/',prob_home,name='sort_tag'),
    path('<int:id>/comment_problem/',comment,name='comment_problem'),
    path('delete_comment/',delete_comment,name='delete_comment'),
    path('edit_comment_problem/',edit_comment,name='edit_comment_problem'),

]
