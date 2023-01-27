# Generated by Django 4.1.3 on 2023-01-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodcenters', '0002_bloodcenter_center_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_name', models.CharField(max_length=45)),
                ('center_region', models.CharField(choices=[('Mumbai', 'Mumbai'), ('Kolkata', 'Kolkata'), ('Delhi', 'Delhi'), ('Vishakhapatnam', 'Vishakhapatnam'), ('Bengaluru', 'Bengaluru'), ('Lucknow', 'Lucknow'), ('Hyderabad', 'Hyderabad'), ('Pune', 'Pune'), ('Goa', 'Goa'), ('Srinagar', 'Srinagar')], default='Vishakhapatnam', max_length=100)),
                ('center_type', models.CharField(default='donation', max_length=40)),
                ('customer_name', models.CharField(max_length=100)),
            ],
        ),
    ]
