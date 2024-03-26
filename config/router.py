from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from orion_management.api.viewsets import StateViewSet, CityViewSet, CountryViewSet, AddressViewSet, BranchViewSet, ClientViewSet, OrganizationViewSet

if settings.DEBUG:
    #It includes the API Root, good for debug
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"state", StateViewSet)
router.register(r"city", CityViewSet)
router.register(r"country", CountryViewSet)
router.register(r"address", AddressViewSet)
router.register(r"branch", BranchViewSet)
router.register(r"client", ClientViewSet)
router.register(r"organization", OrganizationViewSet)

app_name = "api"
urlpatterns = router.urls