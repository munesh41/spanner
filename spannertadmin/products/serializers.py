from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField()
    # content = serializers.CharField(max_length=200)
    # created = serializers.DateTimeField()
    class Meta:
        model = Products
        fields = '__all__'