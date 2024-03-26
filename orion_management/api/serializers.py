from rest_framework import serializers
from django.urls import reverse
from ..utils import BaseUrlMixin
from ..models import State, City, Country, Address, Client, Branch, Organization

class StateSerializer(BaseUrlMixin, serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = State
        fields = ('id', 'url', 'name')
        
class CitySerializer(BaseUrlMixin, serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = City
        fields = ('id', 'url', 'name')

class CountrySerializer(BaseUrlMixin, serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Country
        fields = ('id', 'url', 'name')
        
class AddressSerializer(BaseUrlMixin, serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    state = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())
    city = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())
    country = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())

    class Meta:
        model = Address
        fields = ('id', 'url', 'name', 'street', 'state', 'city', 'country')
        
class BranchSerializer(BaseUrlMixin, serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    address = AddressSerializer()

    class Meta:
        model = Branch
        fields = ('id', 'url', 'name', 'address')
        
class ClientSerializer(BaseUrlMixin, serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    addresses = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all(), many=True)
    cell_phone = serializers.CharField(source='cell_phone.as_e164')
    work_phone = serializers.CharField(source='work_phone.as_e164')
    
    class Meta:
        model = Client
        fields = ('id', 'url', 'name', 'birth_date', 'addresses', 'cell_phone', 'work_phone', 'email')

class OrganizationSerializer(BaseUrlMixin, serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    clients = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), many=True)
    branches = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), many=True)

    class Meta:
        model = Organization
        fields = ('id', 'url', 'name', 'branches', 'clients')
