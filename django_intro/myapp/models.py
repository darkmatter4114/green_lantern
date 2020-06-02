# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=6, decimal_places=0)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Dish(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=6, decimal_places=0)
    name = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dish'


class Meny(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=6, decimal_places=0)
    name = models.CharField(max_length=30, blank=True, null=True)
    id_dish = models.ForeignKey(Dish, models.DO_NOTHING, db_column='id_dish', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meny'


class Personal(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=6, decimal_places=0)
    f_name = models.CharField(max_length=30, blank=True, null=True)
    l_name = models.CharField(max_length=30, blank=True, null=True)
    vacancy = models.CharField(max_length=30, blank=True, null=True)
    restoran = models.ForeignKey('Restoran', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'


class Restoran(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    name = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    street = models.CharField(max_length=2, blank=True, null=True)
    contact = models.CharField(max_length=16, blank=True, null=True)
    phone number  = models.CharField(max_length=12, blank=True, null=True)
    meny = models.ForeignKey(Meny, models.DO_NOTHING, db_column='meny', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restoran'
