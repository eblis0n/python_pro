# dptestWeb/dptestWeb/view.py
from django.conf.urls import url
from . import view

urlpatterns = [
    url(r'^$', view.index),
    url('^yoyo$', view.yoyo),
]