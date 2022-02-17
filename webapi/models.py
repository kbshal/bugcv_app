from django.db import models
from django.contrib.auth.models import User
class PatientHistory(models.Model):
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,related_name="patientHistory")
    patient = models.ForeignKey(User,on_delete=models.CASCADE,related_name="history")
    remark = models.TextField()
    recorded_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("-recorded_on",)
    def __str__(self):
        return self.patient.username