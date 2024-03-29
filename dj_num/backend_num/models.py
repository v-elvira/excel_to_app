from django.db import models

# Create your models here.
# class Test(models.Model):
# 	title = models.CharField(max_length=100)
# 	info = models.CharField(max_length=100)

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Sales(models.Model):
    id = models.IntegerField(primary_key=True)
    contract = models.IntegerField()
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    delivery_date = models.DateField()
    rub_price = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'sales'
