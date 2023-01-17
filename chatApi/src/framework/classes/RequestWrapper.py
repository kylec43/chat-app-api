class RequestWrapper:

    def __init__(self, request):
        self._request = request

    def get(self):
        return self._request
    
    def get_body(self):
        return self._request.GET if self._request.method == 'GET' else self._request.POST

    def get_method(self):
        return self._request.method
