from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from ..models import State, City, Country, Address, Branch, Client, Organization
from .serializers import StateSerializer, CitySerializer, CountrySerializer, AddressSerializer, BranchSerializer, ClientSerializer, OrganizationSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class =  StateSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name','description','created','modified', 'active')

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class =  CitySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name','description','created','modified', 'active')

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class =  CountrySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name','description','created','modified', 'active')
    
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class =  AddressSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name', 'street', 'state', 'city', 'country', 'description','created','modified', 'active')

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class =  BranchSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name', 'address', 'description','created','modified', 'active')

#Allow non-authenticated users to view open positions since it's information that should be public to get people to apply
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class =  ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name', 'birth_date', 'addresses', 'cell_phone', 'work_phone', 'email', 'description','created','modified', 'active')

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class =  OrganizationSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name', 'clients', 'branches', 'description','created','modified', 'active')