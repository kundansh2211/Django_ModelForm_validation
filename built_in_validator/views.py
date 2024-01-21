from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentForm

def student_view(request):
    template = 'built_in_validator/student_form.html'
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data saved!')
    context = {"form": form}
    return render(request, template, context)
