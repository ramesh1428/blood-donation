from django.shortcuts import render,redirect
from bloodcenters.models import BloodCenter

def home(request):
    arr = []
    center = BloodCenter.objects.values('center_region').distinct()
    for i in center:
        arr.append(i)
    return render(request,'index.html',{'center_details':arr})


# def register(request):
#     return render(request,'register.html')

# def login(request):
#     return render(request,'login.html')

# def contactus(request):
#     return render(request,'contact.html')
