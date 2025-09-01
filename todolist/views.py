from django.shortcuts import render , redirect
from django.http import HttpResponse
from todolist.models import Todolist
from todolist.forms import Todoform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist (request):
    if request.method=="POST":
        form=Todoform(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New task added!!"))#message method after you verify and save your form
        return redirect ("todolist")
        
    else:
     all_task=Todolist.objects.all()
     paginator=Paginator(all_task,5)
     page_number=request.GET.get('pg')
     page_obj=paginator.get_page(page_number)
     
     return render(request,'todolist.html',{"page_obj":page_obj})
    
# render( request, html page, content(always in the form of a dictionary))

@login_required
def delete_task (request, id):
    task= Todolist.objects.get(pk=id)
    task.delete()
    return redirect ("todolist")
@login_required
def edit_task (request, id):
    if request.method=="POST":
        task= Todolist.objects.get(pk=id)
        form =Todoform(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited!!"))#message method after you verify and save your form
        return redirect ("todolist")
        
    else:
       task_obj=Todolist.objects.get(pk=id)
       return render(request,'edit.html',{"task_obj":task_obj})
@login_required    
def complete_task (request, id):
    task= Todolist.objects.get(pk=id)
    task.done=True
    task.save()
    return redirect ("todolist")
@login_required
def pending_task (request, id):
    task= Todolist.objects.get(pk=id)
    task.done=False
    task.save()
    return redirect ("todolist")


def contact (request):
    context={ 'contact_text':"Welcome to contacts"}
    return render(request,'contact.html',context)

def about (request):
    context={ 'about_text':"Welcome to about section"}
    return render(request,'about.html',context)

def index (request):
    context={ 'index_text':"Welcome to Home section"}
    return render(request,'index.html',context)



