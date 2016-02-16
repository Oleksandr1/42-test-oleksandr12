from django.shortcuts import render
from models import MyData, RequestHistory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def main_page(request):
    my_data = MyData.objects.first
    return render(request, 'hello/main.html', {'my_data': my_data})


def requests(request):
    req = list(reversed(RequestHistory.objects.all()))
    paginator = Paginator(req, 10)
    page = request.GET.get('page')

    try:
        req = paginator.page(page)
    except PageNotAnInteger:
        req = paginator.page(1)
    except EmptyPage:
        req = paginator.page(paginator.num_pages)

    return render(request, 'hello/requests.html',
                  {'requests': req})
