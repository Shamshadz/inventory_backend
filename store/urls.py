from django.urls import path
from store.views import CompanyView, VehicleView, ItemList , ItemDetail

urlpatterns = [
    # path('items/<str:vehicle>/', ItemsListView.as_view()),
    path('items/', ItemList.as_view(), name='items_list'), #ok
    path('item/<int:pk>/', ItemDetail.as_view(), name='item_detail'), #ok
    path('companies/', CompanyView.as_view()), #ok
    path('vehicles/',VehicleView.as_view()),  #ok
]
