from django.contrib import admin
from .models import State, City, Country, Address, Branch, Client, Organization
# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    list_filter = ['name', 'state', 'city', 'country']
    
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_filter = ['name', 'address']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    list_filter = ['name']

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    list_filter = ['name', 'branches']