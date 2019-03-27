from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


from . import serializers
from . import models
from . import permissions


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
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URL using Routers',
            'Provides more functionality with lesser code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create hello message with a name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles updating objects."""

        return Response({'method': 'retrive'})

    def destroy(self, request, pk=None):
        """Delete an object."""

        return Response({'method': 'destroy'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles Creating,reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email, password and returns authtoken."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and obtain token."""

        return ObtainAuthToken().post(request)


class ProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles Creating,reading and updating profile feed items."""

    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        """Set the user profile to the logged in User."""

        serializer.save(user_profile=self.request.user)
