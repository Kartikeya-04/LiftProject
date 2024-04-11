from django.db import models

# Create your models here.
# Create your models here.
class LiftSystem(models.Model):
    lift_name1=models.CharField(max_length=20)
    lift_name2=models.CharField(max_length=20)

    lift_no = models.IntegerField()
    floor_no=models.IntegerField(max_length=10,default=0)
    time_lift1=models.IntegerField()
    time_lift2=models.IntegerField()
    trigger1=models.IntegerField()
    trigger2=models.IntegerField()

    def __str__(self):
        return self.lift_name     