from rest_framework import serializers
from .models import customer_list

class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer_list
        fields = '__all__'