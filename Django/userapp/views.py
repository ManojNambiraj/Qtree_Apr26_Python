from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

class UserApi(APIView):

    def post(self, request):

        new_user = User(
            name=request.data["name"], 
            age=request.data["age"], 
            email=request.data["email"], 
            mobile=request.data["mobile"], 
            password=request.data["password"]
        )

        new_user.save()

        return Response({'msg': 'Data received successfully'})