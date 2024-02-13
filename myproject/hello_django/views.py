from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from . import views
from django.views import View

class IndexPageView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello World<h1>")



#
# def index(request):
#     return HttpResponse("Hello, world!")
#
#
# def about(request):
#     return HttpResponse("About us")
