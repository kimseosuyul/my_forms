from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import customer_list
from .serializers import CustomerListSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import random

class ApiViewset(viewsets.ModelViewSet):
    queryset = customer_list.objects.all()
    serializer_class = CustomerListSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        item_list = data["item"]
        person_list = data["customer"]
        amount = 0
        call_number = str(person_list['callNumber']).replace("-", "")
        account_number = str(person_list['accountNumber']).replace("-", "")
        for i in item_list.values():
            if i['count'] > 0:
                amount = amount+i['amount']*i['count']

        customer_list.objects.create(
            name= person_list['name'],
            amount = amount,
            account_number = account_number,
            email = person_list['email'],
            call_number = call_number,
            order_list = item_list,
            address = person_list['address'],
            detail_address = person_list['detailAddress'],
            zip_code = person_list['zipCode'],
            memo = person_list['memo'],
            d_name = person_list['memo'],
            d_callNumber = person_list['d_callNumber'],
        )

        return Response(data={"amount":amount}, status=200,)
    

class PaymentConfirmation(viewsets.ModelViewSet):
    queryset = customer_list.objects.all()
    serializer_class = CustomerListSerializer

    def create(self, request):
        data = request.data
        customer_list.objects.filter(id=data["id"]).update(payment=True, random_id=random.randrange(10000000, 100000000))

        return Response(status=200)
    
    def list(self, request):
        id = self.request.query_params.get('id')
        obj = get_object_or_404(customer_list, random_id=id)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
        
    

class MasterViewset(viewsets.ModelViewSet):
    queryset = customer_list.objects.all()
    serializer_class = CustomerListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'call_number', 'account_number', 'payment']

    def list(self, request):
        qureyset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(qureyset, many=True)
        return Response(serializer.data) 
    
    def create(self, request):
        data = request.data
        customer = customer_list.objects.filter(id=data["id"])
        customer.update(payment=False)

        return Response(status=200)
    


                