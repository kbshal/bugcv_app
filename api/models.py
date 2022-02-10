from django.db import models

class BackendData(models.Model):
    name=models.CharField(max_length=20)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['-updated']


# Import part start from here above section was just for testing

class User(models.Model):
    username=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=30)

class Patient(models.Model):
    patient_name=models.CharField(max_length=20)
    patient_age=models.IntegerField()
    patient_number=models.IntegerField()
    patient_address=models.CharField(max_length=20)
    patient_history=models.ForeignKey(BackendData,on_delete=models.CASCADE)



    def __str__(self) -> str:
        return self.username
        