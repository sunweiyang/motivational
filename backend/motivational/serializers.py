from rest_framework import serializers

from .models import Quote, ImageAddress


# Serializers define the API representation.
class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('text', 'author',)


class ImageAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAddress
        fields = ('url',)
