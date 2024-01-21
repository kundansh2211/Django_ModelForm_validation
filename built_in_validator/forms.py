from django import forms
from .models import Student
from django.core import validators

# To Use built-in validators we need to define that field explicitly
class StudentForm(forms.ModelForm):
    roll = forms.IntegerField(validators=[validators.MinValueValidator(1)])
    name = forms.CharField(max_length=20, validators=[validators.MinLengthValidator(2)])

    class Meta:
        model = Student
        fields = '__all__'

