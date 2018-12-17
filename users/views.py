from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:internals'))
def Register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        new_user = form.save()
        authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
        login(request,authenticated_user)
        return HttpResponseRedirect(reverse('app:internals'))
    context = {'form':form}
    return render(request,'register.html',context)
