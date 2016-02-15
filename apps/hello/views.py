from django.shortcuts import render
from models import MyData, RequestHistory
from django.core.paginator import Paginator
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
    req = list(reversed(RequestHistory.objects.all()))
    pag = Paginator(req, 10)
    page_1 = pag.page(1)
    return render(request, 'hello/requests.html',
                  {'requests': page_1.object_list})
