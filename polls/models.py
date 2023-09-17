from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.



class GameModel(models.Model):
    name = models.CharField(max_length=300,default='')
    type = models.CharField(max_length=200,default='')
    time_of_passing = models.DateTimeField(default=datetime.now)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)
    desc = models.TextField(default='Do you like games?')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)


    class Meta:
        db_table = 'GameModel'
    def __str__(self) -> str:
        return self.name