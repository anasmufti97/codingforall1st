from django.shortcuts import render
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("Hello, Django! from HOme")



# def htmlPage(request):
#     return render(request, 'E:\Django\djangoCourse\core\home\Templates\index.html')





from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class UserRegistrationView(APIView):
    def post(self, request, format=None):
        return Response("Post Method")

