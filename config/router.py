from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from orion_management.api.viewsets import StateViewSet, CityViewSet, CountryViewSet, AddressViewSet, BranchViewSet, ClientViewSet, OrganizationViewSet

if settings.DEBUG:
    #It includes the API Root, good for debug
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"state", StateViewSet, basename='state')
router.register(r"city", CityViewSet, basename='city')
router.register(r"country", CountryViewSet, basename='country')
router.register(r"address", AddressViewSet, basename='address')
router.register(r"branch", BranchViewSet, basename='branch')
router.register(r"client", ClientViewSet, basename='client')
router.register(r"organization", OrganizationViewSet, basename='organization')

app_name = "api"
urlpatterns = router.urls