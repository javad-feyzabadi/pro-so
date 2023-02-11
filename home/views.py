from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from . models import Post

class HomeView(View):
    
    def get(self,request):
        posts = Post.objects.all()
        return render(request,'home/index.html',{'posts':posts})


class PostDetailView(View):

    def get(self,request,post_id,post_slug):
        post = Post.objects.get(pk = post_id,slug = post_slug)
        return render(request,'home/detail.html',{'post':post})


class PostDeleteView(LoginRequiredMixin,View):
    
    def get(self,request,post_id):
        post = Post.objects.get(pk = post_id)
        if post.user.id == request.user.id :
            post.delete()
            messages.success(request,"This Post Deleted",'success')
        else:
            messages.error(request,'You cant Delete This Post','danger')
        return redirect('home:home')

         
