from django.urls import path
from .views import home_view,profile_view,update_profile,change_password
urlpatterns = [
    path('',home_view,name='home_view'),
    path('<int:id>/profile/',profile_view,name='profile_view'),
    path('<int:id>/update_profile',update_profile,name='update_profile'),
    path('change_password/',change_password,name='change_password'),
]