from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta,date,time


class Saloon(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255,null=True,blank=True)
    working_starttime =models.TimeField()
    working_endtime = models.TimeField()
    no_of_chairs = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Service(models.Model):
    name =  models.CharField(max_length=255)
    cost = models.FloatField()
    time_required = models.IntegerField()
    saloon = models.ForeignKey(Saloon,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    saloon = models.ForeignKey(Saloon,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    time = models.DateTimeField()
    endtime = models.DateTimeField(null = True, editable=False)

    def save(self, *args, **kwargs):

        now = self.time
        z =now + timedelta(minutes = self.service.time_required)
        self.endtime = z
        super(Booking, self).save()

    def __str__(self):
        return self.service.name




