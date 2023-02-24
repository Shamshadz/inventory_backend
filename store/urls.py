from django.urls import path
from store.views import ItemView, CompanyView, ItemsListView

urlpatterns = [
    path('items/<str:company>', ItemsListView.as_view()),
    path('item/<int:pk>', ItemView.as_view()),
    path('item', ItemView.as_view()),
    path('companies', CompanyView.as_view()),
]
