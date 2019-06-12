from django.contrib.auth.models import User
from django.db import models

from fuelgr import settings


class GasStation(models.Model):
    gasstationid = models.PositiveSmallIntegerField(db_column='gasStationID', primary_key=True)  # Field name made lowercase.
    gasstationlat = models.DecimalField(db_column='gasStationLat', max_digits=10, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    gasstationlong = models.DecimalField(db_column='gasStationLong', max_digits=10, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    fuelcompid = models.IntegerField(db_column='fuelCompID')  # Field name made lowercase.
    fuelcompnormalname = models.CharField(db_column='fuelCompNormalName', max_length=45)  # Field name made lowercase.
    gasstationowner = models.CharField(db_column='gasStationOwner', max_length=128)  # Field name made lowercase.
    ddid = models.CharField(db_column='ddID', max_length=10)  # Field name made lowercase.
    ddnormalname = models.CharField(db_column='ddNormalName', max_length=45)  # Field name made lowercase.
    municipalityid = models.CharField(db_column='municipalityID', max_length=10)  # Field name made lowercase.
    municipalitynormalname = models.CharField(db_column='municipalityNormalName', max_length=45)  # Field name made lowercase.
    countyid = models.CharField(db_column='countyID', max_length=10)  # Field name made lowercase.
    countyname = models.CharField(db_column='countyName', max_length=64)  # Field name made lowercase.
    gasstationaddress = models.CharField(db_column='gasStationAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(max_length=10, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='username')

    class Meta:
        managed=False
        db_table = 'gasstations'


class Order(models.Model):
    orderid = models.AutoField(db_column='orderID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('PriceData', models.DO_NOTHING, db_column='productID')  # Field name made lowercase.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='username')
    quantity = models.PositiveSmallIntegerField()
    when = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class PriceData(models.Model):
    productid = models.AutoField(db_column='productID', primary_key=True)  # Field name made lowercase.
    gasstation = models.ForeignKey(GasStation, models.DO_NOTHING, db_column='gasStationID')  # Field name made lowercase.
    fueltypeid = models.PositiveIntegerField(db_column='fuelTypeID')  # Field name made lowercase.
    fuelsubtypeid = models.PositiveIntegerField(db_column='fuelSubTypeID')  # Field name made lowercase.
    fuelnormalname = models.CharField(db_column='fuelNormalName', max_length=64)  # Field name made lowercase.
    fuelname = models.CharField(db_column='fuelName', max_length=128)  # Field name made lowercase.
    fuelprice = models.DecimalField(db_column='fuelPrice', max_digits=4, decimal_places=3)  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='dateUpdated', blank=True, null=True)  # Field name made lowercase.
    ispremium = models.IntegerField(db_column='isPremium', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pricedata'
        unique_together = (('gasstation', 'fueltypeid', 'fuelsubtypeid'),)
