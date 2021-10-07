from rest_framework import serializers
from EmployeeApp.models import Departments,Employees,Repository

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Repository
        fields='__all__'