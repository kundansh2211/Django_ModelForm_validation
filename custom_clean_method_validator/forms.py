from django import forms
from .models import Employee
from django.core import validators

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def clean_age(self):
        value = self.cleaned_data.get('age')
        if value not in range(1,101):
            raise validators.ValidationError('Age should be in range of 1 to 100..!')
        return value

    def clean_e_id(self):
        value = self.cleaned_data.get('e_id')
        if value.isalnum() == False:
            raise validators.ValidationError('Your ID must contain alpha numeric value. Enter a correct ID.')
        return value

    def clean_name(self):
        value = self.cleaned_data.get('name')
        if value.istitle() == False:
            raise validators.ValidationError('Your First Character of Name  should be in Uppercase..')
        return value

    def clean(self):
        data = super().clean()
        value1 = self.data['password']
        value2 = self.data['c_password']
        if value1 != value2:
            raise validators.ValidationError('Both Passwords should be same!')



