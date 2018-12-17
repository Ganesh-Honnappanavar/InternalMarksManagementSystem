from django.urls import path
from . import views
from django.contrib.auth.views import login

app_name = 'users'

urlpatterns = [
    path('logout/',views.LogoutView,name='logout'),
    path('login/',login,{'template_name':'login.html'},name='login'),
    path('register/',views.Register,name='register'),

]
