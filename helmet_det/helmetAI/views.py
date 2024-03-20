from django.shortcuts import render

# Create your views here.
def home(request):
    template='main/home.html'
    return(render(request,template))
def result(request):
    return(render(request,'result.html'))
