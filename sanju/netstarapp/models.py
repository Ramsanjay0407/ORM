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


