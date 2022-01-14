from django.db import models



class Test(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    #name=first_name+last_name
    time=models.DateTimeField(auto_now=True)

    def __str__(self):
        print(time)
        return self.first_name,self.last_name
    
    
