from django.shortcuts import render,redirect
from .models import *
from .forms import *

def create(request):
    a=StudentForm()
    b = Student.objects.all()
    if request.method == 'POST':
        a= StudentForm(request.POST)
        if a.is_valid():
           a.save()
           return redirect('create')
        else:pass
    else:pass   
    return render(request,'index.html',{'form':a,'data':b})

# def read(request):
#     b = Student.objects.all()
#     return render(request,'read.html',{'data':b})

def edit(request,email):
    c = Student.objects.get(email = email)
    d = Student.objects.all()
    e = StudentForm(instance=c)
    if request.method == 'POST':
        a = StudentForm(request.POST)
        if a.is_valid():
            a.save()
            return redirect('create')
        else:
           pass
    else:
        pass
    return render(request,'index.html',{'form':c,'data':d})
        
def delete(request,id):
    a = Student.objects.get(id=id) 
    a.delete()
    return redirect('create')
    
