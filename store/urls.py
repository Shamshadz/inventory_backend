from django.urls import path
from store.views import CompanyView, VehicleView, ItemList , ItemDetail, ItemsListView, SearchAPIView, ItemSearchView

urlpatterns = [
    path('companies/', CompanyView.as_view()), #ok
    path('vehicles/',VehicleView.as_view()),  #ok
    path('items/', ItemList.as_view(), name='items_list'), #ok
    path('item/<int:pk>/', ItemDetail.as_view(), name='item_detail'), #ok
    path('items/<str:vehicle>/', ItemsListView.as_view()),
    # path('search/',sea/, name='search'),
    path('search/', SearchAPIView.as_view(), name='search'),
    path('searchItem/', ItemSearchView.as_view(), name='searchItem'),
    # http://127.0.0.1:8000/api/store/searchItem/?search=hiran
]
