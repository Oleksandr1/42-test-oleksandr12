from django.shortcuts import render
from models import MyData
# Create your views here.


def main_page(request):
    my_data = MyData.objects.first
    return render(request, 'hello/main.html', {'my_data': my_data})
