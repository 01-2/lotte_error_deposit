from django.db import models

# Create your models here.
class TotalData(models.Model):
    date = models.DateField()
    stkOut = models.PositiveIntegerField()
    dbplay = models.PositiveIntegerField()
    homerun = models.PositiveIntegerField()
    balk = models.PositiveIntegerField()
    passedBall = models.PositiveIntegerField()
    error = models.PositiveIntegerField()

    def __str__(self):
        return str(self.date)