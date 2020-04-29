
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Quote, ImageAddress
from .serializers import QuoteSerializer, ImageAddressSerializer


class QuoteAPIView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        quote = Quote.objects.order_by("?").first()
        return Response({"text": quote.text, "author": quote.author})


class ImageAddressAPIView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    queryset = ImageAddress.objects.all()
    serializer_class = ImageAddressSerializer

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        image_address = ImageAddress.objects.order_by("?").first()
        return Response({"url": image_address.url})