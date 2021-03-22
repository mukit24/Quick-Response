from django.urls import path,include
from .views import prob_home
urlpatterns = [
    path('',prob_home,name='prob_home')
]
