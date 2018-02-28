from rest_framework import serializers
from .models import Client_Detail,Product_Area,Create_Request


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Detail
        fields = ('id','name',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Area
        fields = ('id','product_name',)

class RequestSerializer(serializers.ModelSerializer):
    client_id = ClientSerializer()
    pro_area_id = ProductSerializer()
    class Meta:
        model = Create_Request
        fields = ('req_title','req_description','client_id','pro_area_id','target_date','req_priority','status')


