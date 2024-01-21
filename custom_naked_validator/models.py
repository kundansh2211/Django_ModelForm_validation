from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    c_pass = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.username} {self.password} {self.c_pass}'
