from django.contrib.auth.models import User
from rest_framework import serializers
from restaurant.models import Menu, Restaurant

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
