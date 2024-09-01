from django.db import models

# Create your models here.

class customer_list(models.Model):
    name = models.CharField(max_length=16)
    amount = models.IntegerField()
    account_number = models.CharField(max_length=20)
    email = models.CharField(max_length=64)
    call_number = models.CharField(max_length=13)
    order_list = models.JSONField()
    date = models.DateTimeField(auto_now_add=True)
    payment = models.BooleanField(default=False)
    random_id = models.CharField(max_length=8, blank=True)
    