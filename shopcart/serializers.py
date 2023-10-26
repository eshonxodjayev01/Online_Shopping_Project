from rest_framework import serializers
from .models import Shopcard

class Shopcardserializers(serializers.ModelSerializer):
    class Meta:
        model = Shopcard
        fields = ['id', 'date', 'product', 'owner', 'payment']  # Corrected field name 'praduct' to 'product'

class UpdateShopcardserialazer(serializers.ModelSerializer):
    class Meta:
        model = Shopcard
        fields = ['id', 'date', 'product', 'owner', 'payment']  # Corrected field name 'praduct' to 'product'

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.date = validated_data.get("date", instance.date)
        instance.product = validated_data.get("product", instance.product)  # Corrected field name 'praduct' to 'product'
        instance.owner = validated_data.get("owner", instance.owner)
        instance.payment = validated_data.get("payment", instance.payment)  # Corrected field name 'paymant' to 'payment'
        instance.save()
        return instance
