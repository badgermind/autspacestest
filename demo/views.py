from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name = "about.html"

class AutismPageView(TemplateView):
    template_name = "autism.html"

class HomePageView(TemplateView):
    template_name = "home.html"

class ModeratePageView(TemplateView):
    template_name = "moderate.html"

class MyStoriesPageView(TemplateView):
    template_name = "mystories.html"

class ShareStoriesPageView(TemplateView):
    template_name = "sharestories.html"

class ViewStoriesPageView(TemplateView):
    template_name = "viewstories.html"

class OverviewPageView(TemplateView):
    template_name = "overview.html"

class RegistrationPageView(TemplateView):
    template_name = "registration.html"

class LogoutPageView(TemplateView):
    template_name = "logout.html"


# def homePageView(request):
#     return HttpResponse("Hello, World!")