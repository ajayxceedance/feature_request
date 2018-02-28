from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer,ProductSerializer,RequestSerializer
from .models import Client_Detail,Product_Area,Create_Request
from rest_framework.response import Response
from rest_framework import status
import os,logging,datetime

""" 
fatch the PATH of our base project and join errorLog file with 
base project DIR
"""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILENAME = os.path.join(BASE_DIR,"errorlog.log")
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

# Create our views here.

class ClientList(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving client.
    """
    def list(self, request):
        queryset = Client_Detail.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductList(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Product Area.
    """
    def list(self, request):
        queryset = Product_Area.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateRequest(viewsets.ViewSet):
    """
    A simple ViewSet for creating new feature request from user.
    """
    serializer_class = RequestSerializer

    def create(self, request):
        try:
           data = request.data
           print(data,type(data))
           title = data.get("title")
           description = data.get("description")
           client_obj = Client_Detail.objects.get(pk=data.get("c_id"))
           product_obj = Product_Area.objects.get(pk=data.get("p_id"))
           target_date = data.get("t_date")
           req_priority = data.get("req_priority")
           
           priority_queryset = Create_Request.objects.filter(req_priority__gte=req_priority,
                                                            client_id=client_obj)
           if priority_queryset:
                                for obj in priority_queryset:
                                    obj.req_priority = obj.req_priority+1
                                    obj.save()

           Create_Request.objects.create(req_title=title,req_description=description,
               client_id=client_obj,pro_area_id=product_obj,target_date=target_date,
               req_priority=req_priority)

           return Response(status=status.HTTP_201_CREATED)

        except Exception as error:
           """
           Error Logging with current time 
           """
           now = datetime.datetime.now()
           error = str(now)+" ====> "+str(error)
           logging.debug(error)
           return Response("matching query does not exist",status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """ 
           Gives the list of created feature requests 
        """
        queryset = Create_Request.objects.all()
        serializer = RequestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)












