from django.db import models

# Create your models here.
 
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class Job(models.Model):
    title = models.CharField(max_length=50)
    # locations
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salery = models.IntegerField(default=0)
    exprince = models.IntegerField(default=1)
    category = models.ForeignKey("Category",on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = ("Job")
        verbose_name_plural = ("Jobs")

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.name

