from .models import Job
from .serializers import JobSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all()
    data = JobSerializers(all_jobs, many=True).data
    return Response({'data':data})

@api_view(['GET'])
def job_detail_api(request, id):
    detail_job = Job.objects.get(id=id)
    data = JobSerializers(detail_job).data
    return Response({'data':data})


class JobListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers
    lookup_field = 'id'