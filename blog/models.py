from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=150)
    views = models.IntegerField(default= 0)
    timestamp = models.DateTimeField(blank=True ,default=timezone.now)

    class Meta:
        ordering= ('-timestamp',)
    def __str__(self):
        return self.title +' '+'by'+' ' + self.author

class BlogComment(models.Model):
     sno = models.AutoField(primary_key=True)
     comment = models.TextField()
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     post = models.ForeignKey(Post, on_delete=models.CASCADE)
     parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
     
     timezone = models.DateTimeField(default = now)

     def __str__(self):
         return self.comment[0:12] + "..." + "by" + " " + self.user.username
     


