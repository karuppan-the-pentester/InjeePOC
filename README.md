# InjeePOC

**Injee** is an instant DB config for front-end </br>


## Todo

- [x] Install Injee
- [x] Build or Use template for CRUD
- [x] Set Backend 
- [x] Load some data in injee


## To Install

``` bash
docker pull mindaslab/injee:0.11.0
```


``` bash
docker run -d -p 4125:4125  -v $(pwd)/injee/files:/app/files  -v $(pwd)/injee/views:/app/views  -v $(pwd)/injee/backups:/app/backups  mindaslab/injee:0.11.0
```


``` bash
cd crud-django
```


``` bash
python manage.py runserver
```


## Backend Functions

``` python

# For Read Function 
def index(request):
    if len(requests.get("http://localhost:4125/api/crud").json()) < 1: 
        requests.post("http://localhost:4125/api/crud", json={ 'username' : 'Karthik Raja'}, headers={"Content-Type": "application/json"})

    if("Create" in request.POST):
        return redirect("Create")
    
    return render(request,'index.html',{'data': requests.get("http://localhost:4125/api/crud").json() })

```

``` python

# For Create Function 
def create(request):
    if request.method=='POST':
        username=request.POST.get('username')
        requests.post("http://localhost:4125/api/crud", json={ 'username' : username}, headers={"Content-Type": "application/json"})
        return redirect('Read')
    else:
        print("Request Failed")
    return render(request,'create.html')
```

``` python

# For Update and Delete Functions
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
```



