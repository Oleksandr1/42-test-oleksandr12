from hello.models import RequestHistory


class HistoryRequestMiddleware(object):
    def process_request(self, request):
        req = RequestHistory()
        req.path = request.path_info
        req.post = str(request.POST)
        req.get = str(request.GET)
        req.save()
