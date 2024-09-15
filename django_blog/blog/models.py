from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
class  CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    Profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
# Create your models here.
