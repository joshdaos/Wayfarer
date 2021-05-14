from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import UserProfile

# Create your views here.

class Home(View):
    
    def get(self, request):
        return HttpResponse("Wayfarer Home")


class Home(TemplateView):
    template_name = "home.html"


class UserProfileList(TemplateView):
    template_name = "profile_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Here we are using the model to query the database for us.
        context["profiles"] = UserProfile.objects.all()
        return context
