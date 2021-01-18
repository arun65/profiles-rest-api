from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over ur application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name') # value in name field of our serializer after validations
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST # we can pass status=400 also, its better to use HTTP formats    
            ) # serializer.errors returns a dict of errors based on the validation rules that are applied to the serializer
    
    def put(self, request, pk=None, format=None):
        """Handle updating objects (i.e updates the complete object)"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None, format=None):
        """Handle partial update of objects (i..e updates only fields that are passed in the request)"""
        return Response({'method': 'patch'})
    
    def delete(self, request, pk=None, format=None):
        """Delete an object"""
        return Response({'method': 'delete'})