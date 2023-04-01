from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store.views import ( CompanyView, VCompanyView, VehicleView, ItemList ,
                          ItemDetail, ItemsListView, SearchAPIView, ItemSearchView,
                          DashBoardList, LocationView, LocationDelete)

urlpatterns = [
    path('companies/', CompanyView.as_view()), #ok
    path('vcompanies/', VCompanyView.as_view()), #ok
    path('vehicles/',VehicleView.as_view()),  #ok
    path('items/', ItemList.as_view(), name='items-list'), #ok
    path('item/<int:pk>/', ItemDetail.as_view(), name='item-detail'), #ok
    path('items/<str:vehicle>/', ItemsListView.as_view()),
    path('search/', SearchAPIView.as_view(), name='search'),
    path('searchItem/', ItemSearchView.as_view(), name='searchItem'),
    path('dashboardList/', DashBoardList.as_view(), name='dashBoard-list'), #ok
    path('location/', LocationView.as_view(), name='location'),
    path('locationDelete/<int:pk>', LocationDelete.as_view(), name='location-delete'),
    # http://127.0.0.1:8000/api/store/searchItem/?search=hiran

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
