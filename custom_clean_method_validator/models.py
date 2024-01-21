from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30, verbose_name='Full Name')
    e_id = models.CharField(max_length=10, verbose_name='Employee ID')
    sal = models.FloatField(verbose_name='Salary')
    age = models.IntegerField()
    password = models.CharField(max_length=20, default='password here...')
    c_password = models.CharField(max_length=20, default='same pass here..')

    def __str__(self):
        return f'{self.name} {self.e_id} {self.sal} {self.age}'


