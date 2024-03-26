from django.test import TestCase
from orion_management.models import State, City, Country, Address, Branch, Client, Organization

#Simple Model Unit Test Schema
class OrionManagementTest(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.state = State.objects.create(name='Test State')
        self.city = City.objects.create(name='Test City')
        self.country = Country.objects.create(name='Test Country')
        self.address = Address.objects.create(
            name='Test Address',
            state=self.state,
            city=self.city,
            country=self.country
        )
        self.branch = Branch.objects.create(name='Test Branch', address=self.address)
        self.client = Client.objects.create(
            name='Test Client',
            cell_phone='+1234567890',
            work_phone='+1234567890',
            email='test@example.com'
        )
        self.organization = Organization.objects.create(name='Test Organization')
        self.client.addresses.add(self.address)
        self.organization.clients.add(self.client)
        self.organization.branches.add(self.branch)


    def test_models(self):
        # Test State model
        self.assertEqual(str(self.state), 'Test State')

        # Test City model
        self.assertEqual(str(self.city), 'Test City')

        # Test Country model
        self.assertEqual(str(self.country), 'Test Country')

        # Test Address model
        self.assertEqual(str(self.address), 'Test Address Test Country')

        # Test Branch model
        self.assertEqual(str(self.branch), 'Test Branch')

        # Test Client model
        self.assertEqual(str(self.client), 'Test Client test@example.com')

        # Test Organization model
        self.assertEqual(str(self.organization), 'Test Organization')
        
        # Test Model Relationships
        self.assertEqual(self.address.state, self.state)
        self.assertEqual(self.branch.address, self.address)
        self.assertIn(self.address, self.client.addresses.all())
        self.assertIn(self.client, self.organization.clients.all())
        self.assertIn(self.branch, self.organization.branches.all())
