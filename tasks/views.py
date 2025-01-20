from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("well come to the task managment system")
def show_task(request):
    return HttpResponse("This is our task page")
def show_specific_task(request,id):
    print("id",id)
    print("id type",type(id))
    return HttpResponse(f"this is specific task {id}")
def dashboard(request,id):
    return HttpResponse("This is dashboard")