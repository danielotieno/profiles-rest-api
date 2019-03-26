from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class HelloApiView(APIView):
    """Test Api View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns list of API views features."""

        an_apiview = [
            'Daniel', 'Rita', 'Moses', 'Kevin', 'Bev'
        ]

        return Response(
            {
                'message': 'Hello People!',
                'an_apiview': an_apiview
            }
        )

    def post(self, request):
        """Create hello message with a name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating objects."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request. Only updating fields provided in the request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Delete an object."""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset."""

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrive, update, partial_update)',
            'Automatically maps to URL using Routers',
            'Provides more functionality with lesser code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
