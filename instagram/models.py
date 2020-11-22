from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image',null=False,default=True)
    title = models.CharField(max_length=500,null=True)
    caption = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes=models.IntegerField(null=True, default=0)
    comment = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']


class Profile(models.Model):
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    # profile_photo = CloudinaryField('image',null=True)
    image = models.ImageField(default='avatar.png',upload_to='profile_pictures')
    bio = models.CharField(max_length=400)

    
    

    
    

