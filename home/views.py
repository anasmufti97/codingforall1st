from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, Django! from HOme")



def htmlPage(request):
    return render(request, 'E:\Django\djangoCourse\core\home\Templates\index.html')







