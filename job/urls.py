from django.urls import path
from . import views
from . import api

app_name='jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),

    # api
    path('api/jobs', api.job_list_api, name='list_api'),
    path('api/jobs/<int:id>', api.job_detail_api, name='detail_api'),

    # classed passed views
    path('api/v2/jobs', api.JobListApi.as_view(), name='list_api'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view(), name='job_detail'),


]
