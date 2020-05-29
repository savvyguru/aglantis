from django.db import models
from django.contrib.auth.models import User

def get_user_image_folder(instance, filename):
    return "%s/%s" % (instance.user.username, filename)

#link user to images
class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media',default=None)
    processedimage = models.ImageField(upload_to='media',default=None)
    #image = models.ImageField(upload_to=get_user_image_folder)
    #processedimage = models.ImageField(upload_to=get_user_image_folder)