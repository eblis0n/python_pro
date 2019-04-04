# dptestWeb/dptestWeb/view.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world !  django ~~")
def yoyo(request):
    return HttpResponse("yoyo!  django ~~ ")