from django.shortcuts import render,redirect
from .models import BloodCenter,Booking

# Create your views here.
def center_list(request):
    if request.method == 'POST':
        region = request.POST.get('region')
        center = BloodCenter.objects.filter(center_region=region)
        print(center)

    return render(request,'list.html',{'center':center})

def book(request,id):
    obj = BloodCenter.objects.get(id=id)
    print(obj)
    booking = Booking(center_name=obj.center_name,center_region=obj.center_region,center_type=obj.center_type,customer_name=request.user.first_name)
    booking.save()
    return redirect('home')