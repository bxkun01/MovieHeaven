from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.views.generic import UpdateView
from .models import Profile
from django.urls import reverse_lazy

def register(request):
    if request.method=='POST':
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')

        if len(password)<8:
            messages.error(request,"Password mustn't be less than 8 characters")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        else:
            User.objects.create_user(email=email, username=username, password=password)
            return redirect('login')


    return render(request, 'users/register.html')

def user_login(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Login or Password!')

    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)

def members(request):
    members=User.objects.exclude(username=request.user.username)
    return render(request, 'users/members.html',{'members':members})

def profile(request):
    return render(request, 'users/profile.html')

class ProfileUpdateView(UpdateView):
    model= Profile
    fields= ['image']
    success_url= reverse_lazy('profile')

    #defines which model to update **Very much required shit!!!!!!
    def get_object(self):
        return self.request.user.profile 

    def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)



    
    