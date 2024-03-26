import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")
import django
django.setup()
import random
from django.utils import timezone
from faker import Faker
from orion_management.models import State, City, Country, Address, Branch, Client, Organization

fake = Faker()

# Populate countries
countries = ['United States', 'Canada', 'United Kingdom', 'Australia']
for country_name in countries:
    Country.objects.get_or_create(name=country_name)

# Populate states
states = ['California', 'New York', 'Texas', 'Florida']
for state_name in states:
    State.objects.get_or_create(name=state_name)

# Populate cities
cities = ['Los Angeles', 'New York City', 'Houston', 'Miami']
for city_name in cities:
    City.objects.get_or_create(name=city_name)

# Get existing countries, states, and cities
countries = Country.objects.all()
states = State.objects.all()
cities = City.objects.all()

# Populate addresses
for _ in range(10):
    name = fake.name()
    country = random.choice(countries)
    state = random.choice(states)
    city = random.choice(cities)
    street_address = fake.street_address()
    Address.objects.create(street=street_address, country=country, state=state, city=city, name=name)

# Populate branches
for _ in range(5):
    address = Address.objects.order_by('?').first()  # Get random address
    Branch.objects.create(address=address, name=fake.company())

# Populate clients
for _ in range(20):
    client = Client.objects.create(
        name=fake.name(),
        cell_phone=fake.phone_number(),
        work_phone=fake.phone_number(),
        birth_date=fake.date_of_birth(),
        email=fake.email()
    )
    # Add random addresses to client
    client.addresses.add(*Address.objects.order_by('?')[:random.randint(1, 3)])

# Populate organization
organization = Organization.objects.create(name='Example Organization')

# Add random clients and branches to organization
organization.clients.add(*Client.objects.all().order_by('?')[:5])
organization.branches.add(*Branch.objects.all().order_by('?')[:3])