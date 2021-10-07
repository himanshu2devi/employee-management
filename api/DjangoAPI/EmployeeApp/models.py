from django.db import models

# Create your models here.
PRODUCTS = (
       ("EAD", "EAD"),
       ("EBD", "EBD"),
       ("OSA", "OSA"),
       ("TDM", "TDM"),
   )
   
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

class Repository (models.Model):
    element = models.CharField(max_length=200, null=False, default="")
    xpath = models.CharField(max_length=200, null=False, default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    page_title = models.CharField(max_length=50, null=False, default="")
    popup_title = models.CharField(max_length=50, null=False, default="")
    ns_map = models.CharField(max_length=200, null=False, default="")
    dropdown_values = models.CharField(max_length=200, null=False, default="")
    default_value = models.CharField(max_length=100, null=False, default="")
    product_name = models.CharField(max_length=20,choices=PRODUCTS, default="EAD")