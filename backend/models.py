from django.db import models



class Test(models.Model):
    name=models.TextField()
    time=models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.name)>50:
            return self.name[0:10]
    
    
