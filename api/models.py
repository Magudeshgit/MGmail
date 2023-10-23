from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class mailstat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    creation_date = models.DateField(auto_now=True)
    last_activity = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
