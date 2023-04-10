from django.db import models

# Create your models here.
region = (
    ('Mumbai','Mumbai'),
    ('Kolkata','Kolkata'),
    ('Delhi','Delhi'),
    ('Vishakhapatnam','Vishakhapatnam'),
    ('Bengaluru','Bengaluru'),
    ('Lucknow','Lucknow'),
    ('Hyderabad','Hyderabad'),
    ('Pune','Pune'),
    ('Goa','Goa'),
    ('Srinagar','Srinagar')
)

class foodCenter(models.Model):
    center_name= models.CharField(max_length=45)
    center_region = models.CharField(max_length=100,choices=region, default='Vishakhapatnam')
    center_type = models.CharField(max_length=40,default="donation")
    
class Booking(models.Model):
    center_name= models.CharField(max_length=45)
    center_region = models.CharField(max_length=100,choices=region, default='Vishakhapatnam')
    center_type = models.CharField(max_length=40,default="donation")
    customer_name   = models.CharField(max_length=100)
