from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def todoApp(request):
    todoInfo = Todo.objects.all()
    try:
        if request.method == 'POST':
            searchValue=request.POST.get('searchValue')
            searchToDo=Todo.objects.filter(title__icontains =searchValue)
            print(searchToDo)
        return render(request,'home/index.html',{'todoInfo':searchToDo})
    except:
        return render(request,'home/index.html',{'todoInfo':todoInfo})

def addInfo(request):
    if request.method == 'POST':
        titleInfo=request.POST.get('titleInfo')
        bodyInfo=request.POST.get('bodyInfo')
        try:
           newTodo = Todo(title=titleInfo,body=bodyInfo)
           newTodo.save()
        except :
            print('Somthing Went Wrong')
    return redirect('/')


def editInfo(request,id):
    titleInfo=request.POST.get('titleInfo')
    bodyInfo=request.POST.get('bodyInfo')
    try:
        getToDo=Todo.objects.get(id=id)
        if getToDo:
            getToDo.title=titleInfo
            getToDo.body=bodyInfo
            getToDo.save()
            return redirect('/')
        else:
            return redirect('/')
    except:
        return redirect('/')


def deleteInfo(request):
    if request.method == 'POST':
        form_data=request.POST
        try:
            getInfo = Todo.objects.get(id=form_data['idInfo'])
            getInfo.delete()
        except:
            print('Somthing Went Wrong')    
    return redirect('/')


def doneInfo(request,id):
    try:
        getToDo=Todo.objects.get(id=id)
        if getToDo:
            if getToDo.isDone==True:
                getToDo.isDone=False
                getToDo.save()
            else:
                getToDo.isDone=True
                getToDo.save()
        return redirect('/')
        
    except:
        return redirect('/')