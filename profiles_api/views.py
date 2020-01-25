from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self ,request ,format=None):
        """Return a list of APIVIew Features"""

        an_apiview = [
            'Python 2',
            'python 3',

        ]

        return Response({'message':'Hello !!!','an_apiview':an_apiview})
