from django.db import models

# Create your models here.
class Records(models.Model): 
    
    name=models.CharField(max_length=15)  #compulsory to give length
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    mobile=models.CharField(max_length=15)
    dob=models.CharField(max_length=15)
    role=models.CharField(max_length=10)
    
    def __str__(self):  #python allows you overwriting not overloading
        
        return self.name
        #id will not be returned as it is inbuilt function


