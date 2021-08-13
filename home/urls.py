from django.urls import path
from .views import home_view,profile_view,update_profile,change_password,points_table,notification_op

urlpatterns = [
    path('',home_view,name='home_view'),
    path('<int:id>/profile/',profile_view,name='profile_view'),
    path('<int:id>/profile/<str:msg>/',profile_view,name='profile_required'),
    path('<int:id>/update_profile',update_profile,name='update_profile'),
    path('change_password/',change_password,name='change_password'),
    path('points/',points_table,name='points'),
    path('notification_op/<int:id>/',notification_op,name='notification_op'),
]

# handler404 = "home.views.page_not_found_view"