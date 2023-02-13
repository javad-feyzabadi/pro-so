from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import (PasswordResetView,PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView
)

from .forms import UserRegistrationForm,UserLoginForm
from . models import Relations

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
        is_following = False
        user = get_object_or_404(User,pk = user_id)
        posts = user.posts.all()
        relations = Relations.objects.filter(from_user = request.user,to_user = user)
        if relations.exists():
            is_following = True
        return render(request,'account/profile.html',{'user':user,'posts':posts,'is_following':is_following})


# PasswordReset

class UserPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_done')
    email_template_name = 'account/password_reset_email.html'

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'

# End PasswordReset


# Follow and UnFollow

class UserFollowView(LoginRequiredMixin,View):
    def get(self,request,user_id):
        user = User.objects.get(id = user_id) 
        relations = Relations.objects.filter(from_user = request.user , to_user = user)
        if relations.exists():
            messages.error(request,'You Already This User','danger')
        else:
            Relations(from_user = request.user , to_user = user).save()
            messages.success(request,'You Followed This User','success')
        return redirect('account:user_profile',user.id)

class UserUnFollowView(LoginRequiredMixin,View):
    def get(self,request,user_id):
        user = User.objects.get(id = user_id)
        relations = Relations.objects.filter(from_user = request.user,to_user = user)
        if relations.exists():
            relations.delete()
            messages.success(request,'You UnFollowed This User','success')
        else:
            messages.error(request,'You Are Not Following This User','danger')
        return redirect('account:user_profile', user.id)

# End Follow and UnFollow

