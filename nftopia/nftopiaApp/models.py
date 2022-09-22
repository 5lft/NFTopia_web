from django.db import models

# Create your models here.
class Post(models.Model):
    nickname = models.CharField(max_length=50)
    photo = models.ImageField(blank=False, null=False, upload_to='img')
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.nickname
        