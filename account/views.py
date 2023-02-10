from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm

class Registerview(View):

    def get(self,request):
        form = UserRegistrationForm()
        return render(request,'account/register.html',{'form':form})
