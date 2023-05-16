from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from job.models import Job
# Create your views here.

def send_message(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        email   = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
         

    job_list = Job.objects.all()
    paginator = Paginator(job_list, 4)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'job_list' : page_obj,
    }
    return render(request, 'contact.html', context)