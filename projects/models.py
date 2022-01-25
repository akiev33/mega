from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'