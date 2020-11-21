from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image',null=False,default=True)
    image_name = models.CharField(max_length=500,null=True)
    caption = models.CharField(max_length=3000,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    likes=models.IntegerField(null=True, default=0)
    comment = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image',null=True)
    # image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField()

    def __str__(self):
        return self.user.author
    

    
    

