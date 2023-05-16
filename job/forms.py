from django.forms import ModelForm
from .models import Apply, Job


class ApplyForm(ModelForm):
    
    class Meta:
        model = Apply
        fields = ['name','email','cv','wepsite','cover_letter']

# ------------------------

class JobForm(ModelForm):
    
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug','author')
