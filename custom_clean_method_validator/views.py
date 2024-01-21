from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmployeeForm

def employee_view(request):
    template = 'custom_clean_method_validator/employee.html'
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Successful!')
    context = {"form": form}
    return render(request, template, context)
