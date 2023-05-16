from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
 
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class Job(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    # locations
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salery = models.IntegerField(default=0)
    exprince = models.IntegerField(default=1)
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey("Category",on_delete=models.CASCADE, null=True)
    svg = models.FileField(upload_to='jobs_svg/')
    img = models.ImageField(upload_to='jobs/')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)

    class Meta:
        verbose_name = ("Job")
        verbose_name_plural = ("Jobs")

    def __str__(self):
        return self.title

# ------------------------------------
class Category(models.Model):
    name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.name
    
# ---------------------------
class Apply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name='aplly_jobs', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    wepsite = models.URLField(max_length=200)
    cv = models.FileField(upload_to='aplly/')
    cover_letter = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name