from rest_framework.decorators import api_view
from rest_framework import status, serializers
from rest_framework.response import Response
from .models import Shopcard
from .serializers import Shopcardserializers, UpdateShopcardserialazer
from drf_yasg.utils import swagger_auto_schema

# List all Shopcard objects
@swagger_auto_schema(method='GET')
@api_view(['GET'])
def shopcard_list(request):
    if request.method == 'GET':
        shopcards = Shopcard.objects.all()
        serializer = Shopcardserializers(shopcards, many=True)
        return Response(serializer.data)

# Create a new Shopcard object
@swagger_auto_schema(method='POST', request_body=Shopcardserializers, operation_description="Create a new Shopcard")
@api_view(['POST'])
def shopcard_created(request):
    shopcard = Shopcardserializers(data=request.data)
    if shopcard.is_valid():
        shopcard.save()
        return Response(shopcard.data, status=status.HTTP_201_CREATED)
    return Response(shopcard.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve a specific Shopcard object by ID
@swagger_auto_schema(method='GET')
@api_view(['GET'])
def shopcard_id(request, pk):
    if request.method == 'GET':
        try:
            shopcard = Shopcard.objects.get(id=pk)
            serializer = Shopcardserializers(shopcard)
            return Response(serializer.data)
        except Shopcard.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Update a specific Shopcard object by ID
@swagger_auto_schema(method='PATCH', request_body=UpdateShopcardserialazer, operation_description="Update a Shopcard")
@api_view(['PATCH'])
def shopcard_update(request, pk):
    try:
        shopcard = Shopcard.objects.get(id=pk)
        data = UpdateShopcardserialazer(instance=shopcard, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    except Shopcard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Delete a specific Shopcard object by ID
@swagger_auto_schema(method='DELETE', operation_description="Delete a Shopcard")
@api_view(['DELETE'])
def shopcard_delete(request, pk):
    try:
        shopcard = Shopcard.objects.get(id=pk)
        shopcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Shopcard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
