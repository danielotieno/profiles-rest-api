from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View."""

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
