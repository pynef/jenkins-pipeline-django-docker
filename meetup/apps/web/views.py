from django.shortcuts import render
from django.views.generic import TemplateView

class HomeViews(TemplateView):
    template_name = 'web/home.html'

