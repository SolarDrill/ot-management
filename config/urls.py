from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth.views import LoginView, LogoutView
from .drf_yasg_integration import (
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView
    )

schema_view = get_schema_view(
   openapi.Info(
      title="Orion Management",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('config.router')),  # Include your API's URL configuration
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/api/v1/docs/'), name='logout'),

]

urlpatterns += [
    path('api/v1/token/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', DecoratedTokenRefreshView.as_view(), name='token_refresh')
    ]