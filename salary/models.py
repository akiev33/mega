from django.db import models

from body.models import Employee


class Salary(models.Model):
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    salary = models.PositiveIntegerField()
    
    
    def __str__(self):
        return f'{self.salary} $ -> {self.employee_id}'
    
