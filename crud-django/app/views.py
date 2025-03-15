from django.shortcuts import render,redirect
from .models import CrudDB
# Create your views here.

def index(request):
    un=CrudDB.objects.all()
    if("Create" in request.POST):
        return redirect("Create")
    return render(request,'index.html',{'data':un})

def create(request):
    if request.method=='POST':
        username=request.POST.get('username')
        data=CrudDB(UserName=username)
        data.save()
        print("Request Sended")
        return redirect('Read')
    else:
        print("Request Failed")
    return render(request,'create.html')

def update(request,un_id):
    Data=CrudDB.objects.get(pk=un_id)
    if request.method == 'POST':
        if('Update' in request.POST):
            username = request.POST.get('username')
            Data.UserName=username
            Data.save()
            return redirect('Read')
        elif('Delete' in request.POST):
            Data.delete()
            return redirect('Read')

    else:
        print("Request Failed")
    return render(request,'update.html',{'data':Data.UserName})