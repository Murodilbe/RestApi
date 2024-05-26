from rest_framework import serializers
from .views import Cars
class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'