from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    all_Person = Person.objects.all()
    return render(request, "index.html", {"all_Person": all_Person})

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,"form.html")


def addData(request):
    name = request.POST['name']
    age = request.POST['age']
    

    person = Person.objects.create(name=name, age=age)
    person.save()
    
    return redirect('/')