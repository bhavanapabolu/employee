from django.db import models

class employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    email_address=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)