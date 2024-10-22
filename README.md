# Ex02 Django ORM Web Application
## Date: 22-10-2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<BANK LOAN 23.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
Models.py 

from django.db import models
from django.contrib import admin
class Customer (models.Model):
  cid=models.CharField(max_length=20,primary_key="cid")
  name=models.CharField(max_length=100)
  loanamount=models.IntegerField()
  dob=models.DateField()
  contactnumber=models.IntegerField()

class CustomerAdmin(admin.ModelAdmin):
  list_display=('cid','name','loanamount','dob','contactnumber')

Admin.py
from django.contrib import admin
from .models import Customer,CustomerAdmin
admin.site.register(Customer,CustomerAdmin)

```
## OUTPUT

![alt text](<Screenshot 2024-10-22 150615.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
