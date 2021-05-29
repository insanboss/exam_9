from django.urls import path

from webapp.views.index import index

urlpatterns = [
    path('index/', index, name='index'),
]
