from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Customer
from .serializers import CustomerSerializer, UpdateCustomerSerializer
# 
# # Define a common response schema for successful responses
# success_response = {
#     200: "OK - Request was successful",
# }
# 
# @swagger_auto_schema(method='get', responses=success_response, operation_summary='Retrieve a list of all customers')
# @api_view(['GET'])
# def all_customers(request):
#     customers = Customer.objects.all()
#     serializer = CustomerSerializer(customers, many=True)
#     return Response(serializer.data)
# 
# @swagger_auto_schema(method='get', responses=success_response, operation_summary='Retrieve a specific customer')
# @api_view(['GET'])
# def get_customer(request, pk):
#     customer = get_object_or_404(Customer, pk=pk)
#     serializer = CustomerSerializer(customer)
#     return Response(serializer.data)
# 
# @swagger_auto_schema(method='post', responses={201: "Created - New customer created", 400: "Bad Request - Invalid data"}, operation_summary='Create a new customer')
# @api_view(['POST'])
# def create_customer(request):
#     serializer = CustomerSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
# @swagger_auto_schema(method='patch', responses=success_response, operation_summary='Partially update a customer')
# @api_view(['PATCH'])
# def update_customer(request, pk):
#     customer = get_object_or_404(Customer, pk=pk)
#     serializer = UpdateCustomerSerializer(customer, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
# @swagger_auto_schema(method='delete', responses={204: "No Content - Customer deleted", 404: "Not Found - Customer not found"}, operation_summary='Delete a customer')
# @api_view(['DELETE'])
# def delete_customer(request, pk):
#     customer = get_object_or_404(Customer, pk=pk)
#     customer.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework import status, serializers
from rest_framework.response import Response
from shopcart.models import Shopcard
from .models import Customer
from .serializers import CustomerSerializer, UpdateCustomerSerializer
from shopcart.serializers import UpdateShopcardserialazer,Shopcardserializers

# Use proper naming conventions and avoid naming conflicts
# Use lowercase for variable names

@swagger_auto_schema(method='GET')
@api_view(['GET'])
def the_purchase_price(request, pk):
    if request.method == 'GET':
        shopcard = Shopcard.objects.all()
        customer = Customer.objects.get(id=pk)  # Corrected the variable name
        filtered = [x for x in shopcard if x.owner.id == customer.id]  # Corrected the variable name
        pric = 0
        for item in filtered:  # Changed variable name from i to item for clarity
            pric += item.get_total_price()
        if pric > 1000000:
            data = {"Butun harit": f"1 000 000 so'mdan oshgan va {pric} so'mni tashkil qiladi"}
            return Response(data)
        else:
            data = {"Butun harit": f"1 000 000 so'mdan kam va {pric} so'mni tashkil qiladi"}
            return Response(data)

@swagger_auto_schema(method='GET')
@api_view(['GET'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

@swagger_auto_schema(method='GET')
@api_view(['GET'])
def customer_id(request, pk):
    if request.method == 'GET':
        customer = Customer.objects.get(id=pk)  # Corrected the variable name
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

@swagger_auto_schema(method='POST', request_body=CustomerSerializer, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def customer_created(request):
    customer = CustomerSerializer(data=request.data)
    if Customer.objects.filter(**request.data).exists():  # Use lowercase for the model name
        raise serializers.ValidationError('This data already exists')
    if customer.is_valid():  # Corrected the variable name
        customer.save()
        return Response(customer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='PATCH', request_body=UpdateCustomerSerializer, operation_description="Yangilamaoqchi bo'lgan costumirning ID sini kirting")
@api_view(['PATCH'])
def customer_update(request, pk):
    customer = Customer.objects.get(id=pk)  # Corrected the variable name
    data = UpdateCustomerSerializer(instance=customer, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Customerning ID ni kirting")
@api_view(['DELETE'])
def customer_delete(request, pk):
    if request.method == 'DELETE':
        customer = Customer.objects.get(id=pk)  # Corrected the variable name
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method='GET')
@api_view(['GET'])
def shopcard_list(request):
    if request.method == 'GET':
        shopcards = Shopcard.objects.all()
        serializer = Shopcardserializers(shopcards, many=True)
        return Response(serializer.data)

@swagger_auto_schema(method='GET')
@api_view(['GET'])
def shopcard_id(request, pk):
    if request.method == 'GET':
        shopcard = Shopcard.objects.get(id=pk)
        serializer = Shopcardserializers(shopcard)
        return Response(serializer.data)

@swagger_auto_schema(method='POST', request_body=Shopcardserializers, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def shopcard_created(request):
    shopcard = Shopcardserializers(data=request.data)
    if shopcard.is_valid():
        shopcard.save()
        return Response(shopcard.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='PATCH', request_body=UpdateShopcardserialazer, operation_description="Yangilamaoqchi bo'lgan Shopcardning ID sini kirting")
@api_view(['PATCH'])
def shopcard_update(request, pk):
    shopcard = Shopcard.objects.get(id=pk)
    data = UpdateShopcardserialazer(instance=shopcard, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan shopcardning ID ni kirting")
@api_view(['DELETE'])
def shopcard_delete(request, pk):
    if request.method == 'DELETE':
        shopcard = Shopcard.objects.get(id=pk)
        shopcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
