from rest_framework import serializers
from django.urls import reverse
from ..models import State, City, Country, Address, Client, Branch, Organization

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('id','name','description','created','modified', 'active')
        
class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id','name','description','created','modified', 'active')

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id','name','description','created','modified', 'active')
        
class AddressSerializer(serializers.ModelSerializer):
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())

    class Meta:
        model = Address
        fields = ('id','name', 'street', 'state', 'city', 'country', 'description','created','modified', 'active')
        
class BranchSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())

    class Meta:
        model = Address
        fields = ('id','name', 'address', 'description','created','modified', 'active')
        
        
class ClientSerializer(serializers.ModelSerializer):
    addresses = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all(), many=True)
    cell_phone = serializers.CharField(source='cell_phone.as_e164')
    work_phone = serializers.CharField(source='work_phone.as_e164')
    
    class Meta:
        model = Client
        fields = ('id','name', 'birth_date', 'addresses', 'cell_phone', 'work_phone', 'email', 'description','created','modified', 'active')
        
        
class OrganizationSerializer(serializers.ModelSerializer):
    clients = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), many=True)
    branches = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), many=True)

    class Meta:
        model = Organization
        fields = ('id','name', 'branches', 'clients', 'description','created','modified', 'active')