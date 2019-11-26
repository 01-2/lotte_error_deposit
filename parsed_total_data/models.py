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
    money = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.date)

class SeasonData(models.Model):
    date = models.PositiveIntegerField()
    stkOut = models.PositiveIntegerField()
    dbplay = models.PositiveIntegerField()
    homerun = models.PositiveIntegerField()
    balk = models.PositiveIntegerField()
    passedBall = models.PositiveIntegerField()
    error = models.PositiveIntegerField()
    money = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.date)
