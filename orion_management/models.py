from config.abstract_models import CommonInfo
from .utils import validate_phone_number, validate_email_format
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class State(CommonInfo):
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
    
class City(CommonInfo):
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

class Country(CommonInfo):
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

class Address(CommonInfo):
    street = models.CharField(max_length=100, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, max_length=100)
    city = models.ForeignKey(City,on_delete=models.CASCADE, max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, max_length=100)
    
    def __str__(self):
        return '{0} {1}'.format(self.name, self.country)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        
class Branch(CommonInfo):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

class Client(CommonInfo):
    cell_phone = PhoneNumberField(validators=[validate_phone_number])
    work_phone = PhoneNumberField(validators=[validate_phone_number])
    birth_date = models.DateField(blank=True, null=True)
    addresses = models.ManyToManyField(Address, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, validators=[validate_email_format])
    def __str__(self):
        return '{} {}'.format(self.name, self.email)
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    

class Organization(CommonInfo):
    clients = models.ManyToManyField(Client, blank=True)
    branches = models.ManyToManyField(Branch, blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
    