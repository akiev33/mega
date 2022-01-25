from django.db import models


from positions.models import Position
from projects.models import Project


class Employee(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    fatherland = models.CharField(max_length=60, null=True, blank=True)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.first_name} {self.last_name} - id {self.id}'


class Employees_in_project(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    days_in_project = models.PositiveIntegerField()


    def __str__(self):
        return f'Проект - {self.project_id}, Кол-во дней в проекте: {self.days_in_project}'