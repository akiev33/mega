from django.db import models
from django.forms import CharField

from body.models import Employee


class Addres(models.Model):
    employees = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    name_address = models.CharField(max_length=100)
    mail_index = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.employees} -> {self.name_address}'