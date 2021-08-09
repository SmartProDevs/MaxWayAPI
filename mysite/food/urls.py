from django.urls import path
from .views import *
urlpatterns = [
    path('category-products/', CategoryProductsView.as_view(), name='category-products'),
    path('customer-one/', CustomerView.as_view(), name='customer-one'),
    path('customer-order/', CustomerOrder.as_view(), name='customer-order'),
]