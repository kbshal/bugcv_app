from django.db import models
from django.contrib.auth.models import User

# Import part start from here above section was just for testing


class Patient(models.Model):
    patient_name=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    patient_age=models.IntegerField()
    patient_number=models.IntegerField()
    patient_address=models.CharField(max_length=20)
    patient_history=models.TextField()


    def __str__(self):
        return self.patient_name.username
        