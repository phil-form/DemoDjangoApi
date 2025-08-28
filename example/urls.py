from django.urls import path
from example import views

urlpatterns = [
    path('', views.product_example_all, name='product_example_all'),
]