from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloWorld(request):
    return HttpResponse("Hello World")

def taskList(request):
    return render(request, 'tasks/list.html')