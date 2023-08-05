from store.serializers import (ItemSerializer, CompanySerializer, VCompanySerializer,
                                VehicleSerializer, DashBoardSerializer, DelayTranscationSerializer,
                                 QNotifierSerializer, LoacationSerializer)
from store.models import (ItemModel, CompanyModel, VehicleModel, VCompanyModel, 
                          DashBoardModel, LocationModel, DelayTranscation)
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.db.models import Q
from rest_framework import filters
import os

# Create your views here.

# ok
class CompanyView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = CompanyModel.objects.all()

# ok
class VCompanyView(generics.ListCreateAPIView):
    serializer_class = VCompanySerializer
    queryset = VCompanyModel.objects.all()

# ok
class VehicleView(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer
    queryset = VehicleModel.objects.all()

# ok
class VehicleSearchView(APIView):
    serializer_class = VehicleSerializer

    def get(self, request, format=None):
        query = request.GET['search']

        query_list = filters(query)
        queryset_list  = []

        for query in query_list:
            queryset = VehicleModel.objects.filter(Q(vehicle_name__icontains=query) |
                                                 Q(vcompany__vcompany_name__icontains=query))
            for i in queryset:
                queryset_list.append(i)
            
        queryset_list = [*set(queryset_list)]

        serializer = self.serializer_class(queryset_list, many=True)
        return Response(serializer.data)
    

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
        
        query_list = filters(query)
        queryset_list  = []

        for query in query_list:
            queryset = ItemModel.objects.filter(Q(item_code__icontains=query) | Q(company_name__company_name__icontains=query)|
                                                 Q(vehicle_name__vcompany__vcompany_name__icontains=query) |
                                                Q(vehicle_name__vehicle_name__icontains=query) | Q(description__icontains=query)
                                                | Q(location__icontains=query))
            for i in queryset:
                queryset_list.append(i)
            
        queryset_list = [*set(queryset_list)]

        serializer = self.serializer_class(queryset_list, many=True)
        return Response(serializer.data)
    
def filters(query):
    query_list = query.split(' ')
    return query_list


class DashBoardList(generics.ListCreateAPIView):
    filter_backends = (DynamicSearchFilter,)
    serializer_class = DashBoardSerializer
    queryset = DashBoardModel.objects.all()

class DashBoardSearchView(APIView):
    serializer_class = DashBoardSerializer

    def get(self, request, format=None):
        query = request.GET['date']
       
        query_list = query.split('-')
        
        items = DashBoardModel.objects.filter(created_at__day=query_list[2],
                                              created_at__month=query_list[1],
                                              created_at__year=query_list[0])

        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)


class LocationView(APIView):
    serializer_class = LoacationSerializer

    def get(self, request, format=None):
        query = request.GET['location']
        location = LocationModel.objects.filter(Q(location__icontains=query))

        serializer = self.serializer_class(location, many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, format=None):
        
        serializer = LoacationSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LocationDelete(APIView):
    serializer_class = LoacationSerializer

    def get_object(self, pk):
        try:
            print(LocationModel.objects.get(pk=pk))
            return LocationModel.objects.get(pk=pk)
        except LocationModel.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        print(location)
        if len(location.photo) > 2:
            os.remove(location.photo.path)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class QNotifierList(generics.ListAPIView):
    serializer_class = QNotifierSerializer
    queryset = ItemModel.objects.all()

class DelayTranscationView(generics.ListCreateAPIView):
    serializer_class = DelayTranscationSerializer

    def get_queryset(self):
        try:
            id = self.request.query_params.get('id')
            data = DelayTranscation.objects.get(id=id)
            print("at line 208")
        except:
            is_pending = self.request.query_params.get('is_pending')
            data = DelayTranscation.objects.filter(is_pending=is_pending)
        return data

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(" line 215")
        if self.request.query_params.get('id'):
            serializer = self.serializer_class(queryset)
        else:
            serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TranscationUpdateView(APIView):
    def get_object(self, pk):
        return DelayTranscation.objects.get(pk=pk)

    def patch(self, request, pk):
        DelayTranscation_object = self.get_object(pk)
        serializer = DelayTranscationSerializer(DelayTranscation_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_409_CONFLICT)

    def delete(self, request, pk):
        DelayTranscation_object = self.get_object(pk)
        DelayTranscation_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        



#### Medical views
################################################################################################
###############################################################################################
from store.models import (MedicineCategoryModel, MedicineModel, MedLocationModel, MedDashBoardModel)
from store.serializers import (MedicineCategorySerializer, MedicineSerializer, MedLoacationSerializer, MedDashBoardSerializer, MQNotifierSerializer)

# Create your views here.

# ok
class MedicineCategoryList(generics.ListCreateAPIView):
    serializer_class = MedicineCategorySerializer
    queryset = MedicineCategoryModel.objects.all()

# ok
class MedicineList(generics.ListCreateAPIView):
    serializer_class = MedicineSerializer
    queryset = MedicineModel.objects.all()

# ok
class MedicineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicineModel.objects.all()
    serializer_class = MedicineSerializer

# ok
# class ItemsListView(generics.ListAPIView):
#     serializer_class = MedicineSerializer

#     def get_queryset(self):
#         vehicle = self.kwargs['vehicle']
#         vehicle = MedicineModel.objects.get(vehicle_name=vehicle)
#         return ItemModel.objects.filter(vehicle_name=vehicle.id)

#     def get(self, request, vehicle, format=None):
#         queryset = self.get_queryset()
#         serializer = MedicineSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

    
class MedSearchAPIView(generics.ListAPIView):
    filter_backends = (DynamicSearchFilter,)
    queryset = MedicineModel.objects.all()
    serializer_class = MedicineSerializer


class MedSearchView(APIView):
    serializer_class = MedicineSerializer

    def get(self, request, format=None):
        try:
            query = request.GET['search']

            query_list = filters(query)
            queryset_list  = []

            for query in query_list:
                queryset = MedicineModel.objects.filter(Q(category__category__icontains=query) |
                                                    Q(name__icontains=query) | 
                                                    Q(manufacturer__icontains=query) |
                                                    Q(description__icontains=query) |
                                                    Q(location__icontains=query))
                for i in queryset:
                    queryset_list.append(i)
                
            queryset_list = [*set(queryset_list)]

            serializer = self.serializer_class(queryset_list, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error":str(e), "success":False})


class MedDashBoardList(generics.ListCreateAPIView):
    filter_backends = (DynamicSearchFilter,)
    serializer_class = MedDashBoardSerializer
    queryset = MedDashBoardModel.objects.all()

class MedDashBoardSearchView(APIView):
    serializer_class = MedDashBoardSerializer

    def get(self, request, format=None):
        query = request.GET['date']
       
        query_list = query.split('-')
        
        items = MedDashBoardModel.objects.filter(created_at__day=query_list[2],
                                              created_at__month=query_list[1],
                                              created_at__year=query_list[0])

        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)


class MedLocationView(APIView):
    serializer_class = MedLoacationSerializer

    def get(self, request, format=None):
        query = request.GET['location']
        location = MedLocationModel.objects.filter(Q(location__icontains=query))

        serializer = self.serializer_class(location, many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, format=None):
        
        serializer = MedLoacationSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MedLocationDelete(APIView):
    serializer_class = MedLoacationSerializer

    def get_object(self, pk):
        try:
            return MedLocationModel.objects.get(pk=pk)
        except MedLocationModel.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        if len(location.photo) > 2:
            os.remove(location.photo.path)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MQNotifierList(generics.ListAPIView):
    serializer_class = MQNotifierSerializer
    queryset = MedicineModel.objects.all()
