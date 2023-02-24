from store.serializers import ItemSerializer, CompanySerializer
from store.models import ItemModel, CompanyModel
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

# Create your views here.


class CompanyView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = CompanyModel.objects.all()


class ItemView(APIView):

    def get_object(self, pk):
        print("get_object _called")
        try:
            item = ItemModel.objects.get(pk=pk)
            return item
        except ItemModel.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        print("get _called")
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        print("put_object _called")
        ItemModel = self.get_object(pk)
        serializer = ItemSerializer(ItemModel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        company = self.kwargs['company']
        return ItemModel.objects.filter(vehicle_name=company)

    def get(self, request, comapany, format=None):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
