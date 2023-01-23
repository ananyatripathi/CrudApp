from django.db import models  
class Book(models.Model):  
    bid = models.CharField(max_length=20)  
    bname = models.CharField(max_length=100)  
    bdesc = models.CharField(max_length=1000)  
    bprice = models.CharField(max_length=15)  
    class Meta:  
        db_table = "book"  