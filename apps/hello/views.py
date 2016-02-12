from django.shortcuts import render
from models import MyData, RequestHistory

# Create your views here.


def main_page(request):
    """
    user = User(
                    username='sanya',
                    is_active=True,
                    is_superuser=True,
                    is_staff=True,
                    email='sanya071186@gmail.com')
    user.set_password('11')
    user.save()
    """
    my_data = MyData.objects.first
    return render(request, 'hello/main.html', {'my_data': my_data})


def requests(request):
    req = RequestHistory.objects.all
    return render(request, 'hello/requests.html', {'requests': req})
