from store.serializers import ItemSerializer, CompanySerializer, VehicleSerializer
from store.models import ItemModel, CompanyModel, VehicleModel
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

# Create your views here.

# ok
class CompanyView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = CompanyModel.objects.all()

# ok
class VehicleView(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer
    queryset = VehicleModel.objects.all()

# ok
class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = ItemModel.objects.all()

# ok
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


# 
class ItemsListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        vehicle = self.kwargs['vehicle']
        return ItemModel.objects.filter(vehicle_name=vehicle)

    def get(self, request, vehicle, format=None):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)