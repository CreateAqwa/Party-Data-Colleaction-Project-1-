from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
# from enroll.models import inputIndex
from inputdata.models import data

def index(request):
    return render(request,"index.html")
def help(request):
    return  render(request,"help.html")


def delte(request):
    getdata=data.objects.all()
    viewdata={
        "getdata":getdata
        }
    # print(getdata)
    return render(request,"delte.html",viewdata)



# ============================================================
def insert(request):
    try:
        if request.method=="POST":
# ==========================HTML FILE NAME TAG SET (INSIDE GET)=========================
            name=request.POST.get("name") 
            mobno=request.POST.get("mobno")
            city=request.POST.get("city")
# ==========================HTML FILE NAME TAG SET (INSIDE GET)=========================
            saveddata=data(name=name,mobno=mobno,city=city)
            saveddata.save()
# ===============check Data recived or not -START=================
            # print(name)
            # print(mobno)
            # print(city)
# ===============check Data recived or not -END=================
    except:
        pass
    return render(request,"insert.html")


def delte(request):
    getdata=data.objects.all()
    viewdata={
        "getdata":getdata
        }
    print(getdata)
    return render(request,"delte.html",viewdata)
#===== DELTE CONNECTIED TO DELETEDATA (INPAGE DELTE)=====
def deletedata(request,uid):
    get_id=data.objects.get(id=uid)
    get_id.delete()
    url="/delte/"
    print(uid)
    return HttpResponseRedirect(url)


def update(request,uid):
    get_id=data.objects.get(id=uid)
    internaldata={
        "citylist":["Delhi","Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"],
        "modifydata":get_id
    }
    try:
        if request.method=="POST":
            name=request.POST.get("name")
            mobno=request.POST.get("mobno")
            city=request.POST.get("city")
            newdatachange=data(id=uid,name=name,mobno=mobno,city=city)
            newdatachange.save()
            url="/delte/"
            return HttpResponseRedirect(url)
    except:
        pass
 
    return render(request,"update.html",internaldata)

def viewall(request):
    getdata=data.objects.all()
    viewdata={
        "getdata":getdata
    }
    # print(viewdata)
    return render(request,"viewall.html",viewdata)


