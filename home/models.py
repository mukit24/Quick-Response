from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    profile_picture = models.FileField(upload_to='uploads/')
    batch = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50)
    address = models.CharField(max_length=100,blank=True)
    mobile = models.CharField(max_length=60,blank=True)
    facebook = models.URLField(max_length=60,blank=True)
    total_points = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="volunteer")

    def __str__(self):
        return self.user.username