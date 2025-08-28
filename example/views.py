from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from example.models import ProductExample
from example.serializer import ProductExampleDTOSerializer, ProductExampleFormSerializer

# Create your views here.
@csrf_exempt
def product_example_all(request):
    if request.method == 'GET':
        products = ProductExample.objects.all()
        dtos = ProductExampleDTOSerializer(products, many=True)
        return JsonResponse(dtos.data, status=200, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        form = ProductExampleFormSerializer(data=data)
        if form.is_valid():
            form.save()
            return JsonResponse(form.data, status=201)
        return JsonResponse(form.errors, status=400, safe=False)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def product_example_detail(request, pk):
    try:
        product = ProductExample.objects.get(pk=pk)
    except ProductExample.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    if request.method == 'GET':
        dto = ProductExampleDTOSerializer(product)
        return JsonResponse(dto.data, status=200, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        form = ProductExampleFormSerializer(instance=product, data=data)
        if form.is_valid():
            form.save()
            return JsonResponse(form.data, status=200)
        return JsonResponse(form.errors, status=400, safe=False)
    elif request.method == 'DELETE':
        product.active = False
        product.deletedat = datetime.datetime.now()
        product.save()
        return JsonResponse({'message': 'Product deleted'}, status=204)

    return JsonResponse({'error': 'Method not allowed'}, status=405)