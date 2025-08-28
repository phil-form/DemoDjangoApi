from rest_framework import serializers

from example.models import ProductExample

class ProductExampleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField()
    
    def create(self, validated_data):
        return ProductExample.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.save()
        return instance
    
class ProductExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductExample
        fields = '__all__'