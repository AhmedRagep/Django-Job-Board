from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import ApplyForm, JobForm 
from django.core.paginator import Paginator
from .filters import JobFilter
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    ## Filter
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs

    paginator = Paginator(job_list, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'job_list' : page_obj,
        'num' : job_list,
        'myfilter' : myfilter,
    }
    return render(request, 'job/job_list.html', context)

# ----------------------------
def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.author = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = ApplyForm()

    job_list = Job.objects.all()
    paginator = Paginator(job_list, 4)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    

    context = {
        'job_detail':job_detail,
        'job_list' : page_obj,
        'form' : form,
    }
    return render(request, 'job/job_detail.html', context)


# ------------------------------------

@login_required
def add_job(request):
    if request.method=="POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()

    job_list = Job.objects.all()
    paginator = Paginator(job_list, 4)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'form' : form,
        'job_list' : page_obj,
    }

    return render(request, 'job/add_job.html',context)