from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegistrationForm,UserLoginForm

from home.models import Post


class UserRegisterview(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'],cd['email'],cd['password1'])
            messages.success(request,'your registred successfully','success')
            return redirect('home:home')    
        return render(request,self.template_name,{'form':form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
   
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password = cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'logged in successfully','success')
                return redirect('home:home')
            messages.warning(request,'username and password is wrong','warning')
        return render(request,self.template_name,{'form':form})
        

class UserLogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,"you logged out successfully","success")
        return redirect('home:home')


class UserProfileView(LoginRequiredMixin,View):
    def get(self,request,user_id):
        user = User.objects.get(pk = user_id)
        posts = Post.objects.filter(user = user )
        return render(request,'account/profile.html',{'user':user,'posts':posts})