from rest_framework.views import APIView
from rest_framework.response import Response 


class HelloApiView(APIView):
    """Test API View"""


    def get(self,request, format=None):
        """Returns a list if ApiBView Features"""
        an_apiview = [
            'Uses HTTP mehtods as function (get post,patch,put,delete'
            ''
        ]

        return Response({'message': 'hello', 'an_apiview':an_apiview})