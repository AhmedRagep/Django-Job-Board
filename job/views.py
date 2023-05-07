from django.shortcuts import render
from .models import Job
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    context = {
        'job_list' : job_list,
    }
    return render(request, 'job/jobs.html', context)

def job_detail(request, id):
    job_detail = Job.objects.get(id=id)
    context = {
        'job_detail':job_detail,
    }
    return render(request, 'job/job_details.html', context)