from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request): 
    return render(request,'page/myapp.html')
def contact(request):
    return render(request, 'page/contact.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'page/register.html', {'form': form})
