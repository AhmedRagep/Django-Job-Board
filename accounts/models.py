from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    city = models.ForeignKey("City", related_name='user_city', on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=50)
    img = models.ImageField(upload_to='profile/')
    

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return str(self.user)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    

