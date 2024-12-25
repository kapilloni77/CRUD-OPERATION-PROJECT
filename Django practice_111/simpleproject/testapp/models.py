from django.db import models

class Product(models.Model):
    pname=models.CharField(max_length=60)
    price=models.FloatField()
    pid=models.IntegerField()
    pur_date=models.DateField()

    def get_absolute_url(self):
        return "/list"

        
