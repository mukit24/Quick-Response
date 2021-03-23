from django.urls import path,include
from .views import prob_home,create_problem
urlpatterns = [
    path('',prob_home,name='prob_home'),
    path('create/',create_problem,name='create_problem'),
]
