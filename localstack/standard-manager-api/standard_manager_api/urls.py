"""standard_manager_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Standard Manager API",
        default_version='v1',
        description="Test description",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from rest_api import views

# Default Routes
router = routers.DefaultRouter()
router.register('api', views.ApiViewSet, basename="api")

# # Api Routes (Both versions v1 e v2)
api_router = routers.DefaultRouter()
api_router.register(r'standard', views.StandardViewSet)
api_router.register(r'users', views.UserViewSet)
api_router.register(r'groups', views.GroupViewSet)

# Join the api registries
router.registry.extend(api_router.registry)

# TODO
# https://stackoverflow.com/questions/58384549/drf-yasg-provides-wrong-paths-to-uris

"""

A JSON view of your API specification at /swagger.json
A YAML view of your API specification at /swagger.yaml
A swagger-ui view of your API specification at /swagger/
A ReDoc view of your API specification at /redoc/

"""
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', views.info, name='ping'),
    path('ping/', views.ping, name='ping'),
    path('alive/', views.alive, name='alive'),



    url(r'^v1/', include((api_router.urls, "rest_api"), namespace='v1')),
    url(r'^v2/', include((api_router.urls, "rest_api"), namespace='v2')),

    # swagger routes
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^documentation/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
