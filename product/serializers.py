from rest_framework import serializers
from .models import Category, Product

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class UpdateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'category_id', 'price', 'produced_data', 'expired_data')

class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'category_id', 'price', 'produced_data', 'expired_data']

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.image = validated_data.get("image", instance.image)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.price = validated_data.get("price", instance.price)
        instance.produced_data = validated_data.get("produced_data", instance.produced_data)
        instance.expired_data = validated_data.get("expired_data", instance.expired_data)
