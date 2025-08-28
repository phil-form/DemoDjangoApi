from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from example.models import ProductExample
from example.serializer import ProductExampleModelSerializer, ProductExampleSerializer

# Create your views here.
@csrf_exempt
def product_example_all(request):
    if request.method == 'GET':
        products = ProductExample.objects.all()
        form = ProductExampleModelSerializer(products, many=True)
        return JsonResponse(form.data, status=200, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        form = ProductExampleSerializer(data=data)
        if form.is_valid():
            form.save()
            return JsonResponse(form.data, status=201)
        return JsonResponse(form.errors, status=400, safe=False)