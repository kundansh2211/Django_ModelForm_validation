from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse


def user_view(request):
    template = 'custom_naked_validator/user_form.html'
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User Created')

    context = {"form": form}
    return render(request, template, context)
