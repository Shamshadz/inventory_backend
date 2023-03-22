from store.serializers import ItemSerializer, CompanySerializer, VehicleSerializer
from store.models import ItemModel, CompanyModel, VehicleModel
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.db.models import Q
from rest_framework import filters

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


# ok
class ItemsListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        vehicle = self.kwargs['vehicle']
        vehicle = VehicleModel.objects.get(vehicle_name=vehicle)
        return ItemModel.objects.filter(vehicle_name=vehicle.id)

    def get(self, request, vehicle, format=None):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
def search(request):

    query = request.GET['query']
    print(query)

    if len(query) <1 or len(query) > 50:
        query = []
    else:
        items = ItemModel.objects.filter(Q(item_code__icontains=query) | Q(location__icontains=query))

        print(items)                  


    return Response( status=status.HTTP_200_OK)
# company = CompanyModel.objects.filter(Q(company_name__icontains=query))
# vehicle = CompanyModel.objects.filter(Q(vehicle_name__icontains=query))

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
    

class SearchAPIView(generics.ListAPIView):
    filter_backends = (DynamicSearchFilter,)
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


class ItemSearchView(APIView):
    serializer_class = ItemSerializer

    def get(self, request, format=None):
        query = request.GET['search']
        queryset = ItemModel.objects.filter(Q(item_code__icontains=query) | Q(company_name__company_name__icontains=query) |
                                             Q(vehicle_name__vehicle_name__icontains=query) | Q(description__icontains=query)
                                            | Q(loction__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query))
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)