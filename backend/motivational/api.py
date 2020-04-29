
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Quote, ImageAddress


class QuoteAPIView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        quote = Quote.objects.order_by("?").first()
        return Response(quote)


class ImageAddressAPIView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        image_address = ImageAddress.objects.order_by("?").first()
        return Response(image_address)
