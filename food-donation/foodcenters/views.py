from django.shortcuts import render,redirect
from .models import foodCenter,Booking
from django.contrib import messages

# Create your views here.
def center_list(request):
    if request.method == 'POST':
        region = request.POST.get('region')
        center = foodCenter.objects.filter(center_region=region)
        print(center)

    return render(request,'list.html',{'center':center})

def book(request,id):
    obj = foodCenter.objects.get(id=id)
    print(obj)
    booking = Booking(center_name=obj.center_name,center_region=obj.center_region,center_type=obj.center_type,customer_name=request.user.first_name)
    booking.save()
    messages.info(request,'booking done')
    return redirect('home')