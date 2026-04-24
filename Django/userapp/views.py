from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

class UserAPI(APIView):
    def post(self, request):
        
        UserData = User(
            name=request.data["name"],
            age=request.data["age"],
            email=request.data["email"],
            mobile=request.data["mobile"],
            password=request.data["password"]
        )

        UserData.save()

        return Response({'msg': 'User created successfully'})

    def get(self, request):
         
        usersdata = User.objects.all()

        usersList = []

        for user in usersdata:
            usersList.append({
                'id': user.id,
                'name': user.name,
                'age': user.age,
                'email': user.email,
                'mobile': user.mobile,
                'password': user.password
            })

        return Response(usersList)
    
    def put(self, request, user_id):
        userdata = User.objects.filter(id = user_id)

        if not userdata.exists():
            return Response({'msg': 'User not found'}, status=404)
        else:
            userdata.update(
                name=request.data["name"],
                age=request.data["age"],
                email=request.data["email"],
                mobile=request.data["mobile"],
                password=request.data["password"]
            )

        return Response({'msg': 'User updated successfully'})
    
    def delete(self, request, user_id):

        userdata = User.objects.filter(id = user_id)

        if not userdata.exists():
            return Response({'msg': 'User not found'}, status=404)
        else:
            userdata.delete()

        return Response({'msg': 'User deleted successfully'})