from rest_framework import permissions

from fuels.models import GasStation, PriceData, Order


def absolute(request):
    urls = {
        'ABSOLUTE_ROOT': request.build_absolute_uri('/')[:-1].strip("/"),
        'ABSOLUTE_ROOT_URL': request.build_absolute_uri('/').strip("/"),
    }

    return urls


class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow only gasstation owners to access
    """
    message = "You must be he owner of the gas station"

    def has_permission(self, request, view):
        # Επιτρέπεται η κλήση στο /pricedata/pk/
        if request.build_absolute_uri('?').split('/')[-2] == 'pricedata' and request.method == "GET":
            return  True

        if 'pk' in view.kwargs:
            if request.method == "GET":
                pk = view.kwargs['pk']
                print('In permissions gasstation id :', pk)
                try:
                    gasstation = GasStation.objects.get(gasstationid=pk)
                except:
                    return False
                return gasstation.user.username == request.user.username
            else:
                pk = view.kwargs['pk']
                print('In IsOwner permission order_id :', pk)
                try:
                    gasstation = Order.objects.get(orderid=pk).productid.gasstation
                except:
                    return False
                return gasstation.user.username == request.user.username

        if 'pricedata' in view.kwargs:
            pricedata_id = view.kwargs['pricedata']
            gasstation = PriceData.objects.get(productid = pricedata_id).gasstation
            return gasstation.user.username == request.user.username

        return False



