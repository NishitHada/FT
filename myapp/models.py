from django.db import models

# Create your models here.


class User(models.Model):
    id = models.CharField(max_length=9, primary_key=True, default='404')
    real_name = models.CharField(max_length=60, blank=True, null=True)
    tz = models.CharField(max_length=60, default='INDIA', blank=True, null=True)

    # def __str__(self):
    #     return self.id


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activity_periods")
    start_time = models.DateTimeField(default='2020-02-10 11:34:35', blank=True, null=True)
    end_time = models.DateTimeField(default='2020-02-10 11:34:35', blank=True, null=True)

    # def __str__(self):
    #     return self.id

