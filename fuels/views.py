import datetime
from django.db.models import Count, Min, Max, Avg
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from fuels.permissions import IsOwner
from fuels.models import GasStation, PriceData, Order
from fuels.serializers import GasStationSerializer, PriceDataAndStationSerializer, StatisticsSerializer, \
    GasStationDetailsSerializer, OrderSerializer, PriceDataSerializer, PriceDataTypesSerializer


class FuelPriceDataView(APIView):

    def get(self, req, fuel):
        prices_stations = PriceData.objects.filter(fueltypeid=fuel).order_by('fuelprice')
        serializer = PriceDataAndStationSerializer(prices_stations, many=True)
        return Response(serializer.data)


class PriceDataTypesView(APIView):

    def get(self, req):
        data_types = PriceData.objects.order_by('fueltypeid').values('fueltypeid', 'fuelnormalname').distinct()

        if data_types:
            serialιzer = PriceDataTypesSerializer(data_types, many=True)
            return Response(serialιzer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)


class PriceDataDetailsAndUpdateView(APIView):
    permission_classes = (IsOwner, )

    def get(self,req, pricedata):
        try:
            price_data = PriceData.objects.get(productid=pricedata)
            serializer = PriceDataSerializer(price_data)
            return Response(serializer.data)
        except PriceData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={
                'reason': 'Price data not found for the requested pk'
            })

    def put(self, req, pricedata):
        try:
            price_data = PriceData.objects.get(productid=pricedata)
            self.check_object_permissions(self.request, price_data)
            data = req.data
            data['dateupdated'] = datetime.datetime.utcnow()
            serializer = PriceDataSerializer(price_data, data=req.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
        except PriceData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={
                'reason': 'Price data not found for the requested pk'
            })


class GasStationDetailsView(RetrieveAPIView):
    queryset = GasStation.objects.all()
    serializer_class = GasStationDetailsSerializer


class GasStationListView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = GasStation.objects.all()
    serializer_class = GasStationSerializer


class StatisticsView(APIView):

    def get(self, req, fueltypeid):
        stats = GasStation.objects.filter(pricedata__fueltypeid=fueltypeid).aggregate(gasstations_count=Count('gasstationid', distinct=True), min_price=Min('pricedata__fuelprice'), max_price=Max('pricedata__fuelprice'), avg_price=Avg('pricedata__fuelprice'))
        serializer = StatisticsSerializer(stats)
        return Response(serializer.data)


class OrderListAndDeleteView(ListAPIView):
    model = Order
    serializer_class = OrderSerializer
    permission_classes = (IsOwner, )

    def get_queryset(self):
        gasstation_id = self.kwargs['pk']
        queryset = Order.objects.filter(productid__gasstation = gasstation_id)
        return queryset.order_by('-when')

    def delete(self, req, pk):

        try:
            order = Order.objects.get(orderid = pk)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class OrderView(APIView):

    permission_classes = (permissions.IsAuthenticated, )

    def post(self, req):
        data = req.data
        data['user'] = req.user.username
        data['when'] = datetime.datetime.utcnow()

        order = Order()
        serializer = OrderSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)

        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, data={
            'reason': 'Request data not properly structured'
        })
