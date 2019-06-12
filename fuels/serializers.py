from rest_framework import serializers

from accounts.serializers import UserSerializer
from fuels.models import GasStation, PriceData, Order


class PriceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceData
        fields = '__all__'


class GasStationDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        depth = 1
        model = GasStation
        fields = ('gasstationid', 'gasstationlat', 'gasstationlong', 'fuelcompid', 'fuelcompnormalname', 'gasstationowner', 'ddid', 'ddnormalname', 'municipalityid', 'municipalitynormalname',
                  'countyid', 'countyname', 'gasstationaddress', 'phone1', 'user', 'pricedata_set',)


class GasStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasStation
        fields = '__all__'


class PriceDataTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PriceData
        fields = ('fueltypeid', 'fuelnormalname')


class PriceDataAndStationSerializer(serializers.ModelSerializer):
    gasstation = GasStationSerializer
    class Meta:
        depth = 1
        model = PriceData
        fields = ('productid', 'fuelnormalname', 'fuelsubtypeid', 'fuelprice', 'gasstation')


class StatisticsSerializer(serializers.Serializer):
    gasstations_count = serializers.IntegerField()
    min_price = serializers.DecimalField(max_digits=None, decimal_places=3)
    max_price = serializers.DecimalField(max_digits=None, decimal_places=3)
    avg_price = serializers.DecimalField(max_digits=None, decimal_places=3)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
