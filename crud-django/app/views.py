from django.shortcuts import render,redirect
import requests

#from .models import CrudDB
# Create your views here.

def index(request):
    if("Create" in request.POST):
        return redirect("Create")
    return render(request,'index.html',{'data': requests.get("http://localhost:4125/api/crud").json() })

def create(request):
    if request.method=='POST':
        username=request.POST.get('username')
        requests.post("http://localhost:4125/api/crud", { 'username' : username})
        return redirect('Read')
    else:
        print("Request Failed")
    return render(request,'create.html')

def update(request,un_id):
    if request.method == 'POST':
        if('Update' in request.POST):
            username = request.POST.get('username')
            requests.put("http://localhost:4125/api/crud/"+str(un_id), { 'username' : username})
            return redirect('Read')
        elif('Delete' in request.POST):
            requests.delete("http://localhost:4125/api/crud/"+str(un_id))
            return redirect('Read')

    else:
        print("Request Directly Hitted")
    return render(request,'update.html',{'data':requests.get("http://localhost:4125/api/crud/"+str(un_id)).json()['username'] })
