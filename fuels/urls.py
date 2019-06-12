from django.urls import path
from .views import (
    GasStationListView,
    FuelPriceDataView,
    StatisticsView, GasStationDetailsView, OrderView, PriceDataDetailsAndUpdateView, OrderListAndDeleteView, PriceDataTypesView)

urlpatterns = [
    path('gasstations/', GasStationListView.as_view(), name='fuel-stations'),
    path('pricedata/fueltypes/', PriceDataTypesView.as_view(), name='fuel-pricedata-types'),
    path('pricedata/<int:fuel>/gasstations/', FuelPriceDataView.as_view(), name='fuel-prices'),
    path('pricedata/<int:pricedata>', PriceDataDetailsAndUpdateView.as_view(), name='fuel-pricedata'),
    path('statistics/<int:fueltypeid>/', StatisticsView.as_view(), name='fuel-statistics'),
    path('gasstations/<int:pk>/pricelist/', GasStationDetailsView.as_view(), name='fuel-station-details'),
    path('order/', OrderView.as_view(), name='fuel-order'),
    path('order/<int:pk>/', OrderListAndDeleteView.as_view()),
]
