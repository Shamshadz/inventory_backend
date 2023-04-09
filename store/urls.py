from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store.views import ( CompanyView, VCompanyView, VehicleView, ItemList ,
                          ItemDetail, ItemsListView, SearchAPIView,
                          VehicleSearchView, ItemSearchView, DashBoardSearchView,
                          DashBoardList, LocationView, LocationDelete,
                          QNotifierList, MedicineList, MedicineDetail, MedSearchAPIView, MedSearchView ,
                          MedDashBoardList, MedDashBoardSearchView, MedLocationView,
                          MedLocationDelete, MQNotifierList, )


urlpatterns = [
    path('companies/', CompanyView.as_view()), #ok
    path('vcompanies/', VCompanyView.as_view()), #ok
    path('vehicles/',VehicleView.as_view()),  #ok
    path('searchVehicle/', VehicleSearchView.as_view(),name='vehicle-list'),  #ok
    path('items/', ItemList.as_view(), name='items-list'), #ok
    path('item/<int:pk>/', ItemDetail.as_view(), name='item-detail'), #ok
    path('items/<str:vehicle>/', ItemsListView.as_view()),
    path('search/', SearchAPIView.as_view(), name='search'),
    ## https://shamhadchoudhary.pythonanywhere.com/api/store/search/?search=hero&search_fields=vehicle_name__vcompany__vcompany_name
    path('searchItem/', ItemSearchView.as_view(), name='searchItem'), 
    ## http://127.0.0.1:8000/api/store/searchItem/?search=query
    path('dashboardList/', DashBoardList.as_view(), name='dashBoard-list'), #ok
    # http://127.0.0.1:8000/api/store/dashboardList/?search=230&search_fields=sold_at
    path('dashboard/', DashBoardSearchView.as_view(), name='dashBoard-search'), # ok
    # http://127.0.0.1:8000/api/store/dashboard/?date=date
    path('location/', LocationView.as_view(), name='location'),
    ## http://127.0.0.1:8000/api/store/location/?location=
    path('locationDelete/<int:pk>', LocationDelete.as_view(), name='location-delete'),
    # http://127.0.0.1:8000/api/store/searchItem/?search=hiran
    path('qNotifier/',QNotifierList.as_view(), name='quantity-notifier'),

] + [
    ## medical url patterns
    path('medicines/', MedicineList.as_view(), name='medicines-list'), #ok
    path('medicine/<int:pk>/', MedicineDetail.as_view(), name='medicine-detail'), #ok
    # path('items/<str:vehicle>/', ItemsListView.as_view()),
    path('medSearch/', MedSearchAPIView.as_view(), name='med-search'),
    ## https://shamhadchoudhary.pythonanywhere.com/api/store/medSearch/?search=hero&search_fields=vehicle_name__vcompany__vcompany_name
    path('searchMed/', MedSearchView.as_view(), name='searchMed'), 
    ## http://127.0.0.1:8000/api/store/searchItem/?search=query
    path('medDashboardList/', MedDashBoardList.as_view(), name='med-dashBoard-list'), #ok
    # http://127.0.0.1:8000/api/store/dashboardList/?search=230&search_fields=sold_at
    path('medDashboard/', MedDashBoardSearchView.as_view(), name='med-dashBoard-search'), # ok
    # http://127.0.0.1:8000/api/store/dashboard/?date=date
    path('medLocation/', MedLocationView.as_view(), name='med-location'),
    ## http://127.0.0.1:8000/api/store/location/?location=
    path('medLocationDelete/<int:pk>', MedLocationDelete.as_view(), name='med-location-delete'),
    # http://127.0.0.1:8000/api/store/searchItem/?search=hiran
    path('mqNotifier/',MQNotifierList.as_view(), name='med-quantity-notifier'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

