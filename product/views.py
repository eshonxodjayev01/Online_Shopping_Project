from .models import Category, Product
from .serializers import CategorySerializers, ProductSerializers, UpdateProductSerializer, UpdateCategorySerializer
from rest_framework.decorators import api_view
from rest_framework import status, serializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from datetime import date
from customer.models import Customer
from shopcart.models import Shopcard

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def expired(request):
    if request.method == 'GET':
        products = Product.objects.all()
        filtered = [x for x in products if x.end_data is not None and date.today() > x.end_data]
        serializer = ProductSerializers(filtered, many=True)
        return Response(serializer.data)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def shop_sell_total(request):
    if request.method == 'GET':
        products = Product.objects.all()
        total = 0
        for product in products:
            total += product.price
        response_data = {'shop_sell_total': total}
        return Response(response_data)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def best_selling_product(request):
    if request.method == 'GET':
        shopcards = Shopcard.objects.all()
        products = [x.product.all() for x in shopcards]
        filtered = max(set(products), key=products.count)
        serializer = ProductSerializers(filtered, many=True)
        return Response(serializer.data)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def categoriy(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializers(categories, many=True)
        return Response(serializer.data)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def categoriy_id(request, pk):
    if request.method == 'GET':
        category = Category.objects.get(id=pk)
        serializer = CategorySerializers(category)
        return Response(serializer.data)

@swagger_auto_schema(method='POST', request_body=CategorySerializers, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def categoriy_created(request):
    category = CategorySerializers(data=request.data)
    if Category.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if category.is_valid():
        category.save()
        return Response(category.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='PATCH', request_body=UpdateCategorySerializer,
                     operation_description="Yangilamaoqchi bo'lgan Categoriyaning ID sini kirting")
@api_view(['PATCH'])
def categoriy_update(request, pk):
    category = Category.objects.get(id=pk)
    data = CategorySerializers(instance=category, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan catigoriyning ID ni kirting")
@api_view(['DELETE'])
def categoriy_delete(request, pk):
    if request.method == 'DELETE':
        category = Category.objects.get(id=pk)
        category.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def Product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def Product_id(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

@swagger_auto_schema(method='POST', request_body=ProductSerializers, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def Product_created(request):
    product = ProductSerializers(data=request.data)
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='PATCH', request_body=UpdateProductSerializer,
                     operation_description="Yangilamaoqchi bo'lgan pradukniing ID sini kirting")
@api_view(['PATCH'])
def Product_update(request, pk):
    product = Product.objects.get(id=pk)
    data = ProductSerializers(instance=product, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Praducningning ID ni kirting")
@api_view(['DELETE'])
def Product_delete(request, pk):
    if request.method == 'DELETE':
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
