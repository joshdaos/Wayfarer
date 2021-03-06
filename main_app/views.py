from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import UserProfile, Posts
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView


# Create your views here.

class Home(View):
    
    def get(self, request):
        return HttpResponse("Wayfarer Home")


class Home(View):
   
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "home.html", context)



@method_decorator(login_required, name='dispatch')
class UserProfileList(TemplateView):
    template_name = "profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Here we are using the model to query the database for us.
        context["profile"] = UserProfile.objects.get(user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class PostDetail(DetailView):
    model = Posts
    template_name = "post_detail.html"
    

@method_decorator(login_required, name='dispatch')
class UserProfileUpdate(UpdateView):
     model = UserProfile
     fields = ['name','currentcity','image']
     template_name = "profile_update.html"
     success_url ="/profile/" 



class Signup(View):

    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        
        form = UserCreationForm(request.POST)

        name = request.POST.get("name")
        currentcity = request.POST.get("currentcity")
        image = request.POST.get("image")
    
        if form.is_valid():
            
            user = form.save()
            UserProfile.objects.create(name=name, currentcity=currentcity, image=image, user=user)
            login(request, user)
            return redirect("profile_detail")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
