from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action

from rest_api.v1.models import Standard
from rest_api.v1.serializers import UserSerializer, GroupSerializer, ApiSerializer, StandardSerializer
from rest_api.v2.serializers import StandardSerializer as StandardSerializerV2
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response


@csrf_exempt
@swagger_auto_schema(operation_description="GET /info/")
def info(request):
    return JsonResponse({
        "apiVersion": "0.0.1",
        "apiName": "standard-manager-api",
        "apiArchVersion": "V1",
    })


@swagger_auto_schema(operation_description="GET /alive/")
def alive(request):
    return JsonResponse({"message": "200 OK"})


@swagger_auto_schema(operation_description="GET /ping/")
def ping(request):
    return JsonResponse({"message": "PONG"})


class ApiViewSet(viewsets.ViewSet):
    serializer_class = ApiSerializer

    def list(self, request):
        return Response({
            "apiVersion": "0.0.1",
            "apiName": "standard-manager-api",
            "apiArchVersion": "V1",
        })


#
#     @action(methods=['GET'], detail=False, url_path='alive/', url_name='alive')
#     def alive(self, request):
#         return Response({"message": "OK"})
#
#     @action(methods=['GET'], detail=False)
#     def ping(self, request):
#         return Response({"message": "PONG"})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class StandardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Standard.objects.all()

    # serializer_class = StandardSerializer

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return StandardSerializer
        return StandardSerializerV2
