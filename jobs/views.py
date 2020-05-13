from django.shortcuts import render

from jobs.models import Job

def homepage(request):
    jobs = Job.objects
    return render(request, 'Portfolio/index.html', {'jobs':jobs})

def theme(request):
    return render(request, 'jobs/theme.html')

def login(request):
    return render(request, 'jobs/login.html')

def register(request):
    return render(request, 'jobs/register.html')
