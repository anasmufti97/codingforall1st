from django.shortcuts import render
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("Hello, Django! from HOme")



# def htmlPage(request):
#     return render(request, 'E:\Django\djangoCourse\core\home\Templates\index.html')





from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from home.serializers import UserRegistrationSerializer



class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

