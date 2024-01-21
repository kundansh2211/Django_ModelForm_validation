from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    c_pass = models.CharField(max_length=20, verbose_name='Confirm Password: ')

    def __str__(self):
        return f'{self.name}  {self.city}  {self.roll} {self.password} {self.c_pass}'

