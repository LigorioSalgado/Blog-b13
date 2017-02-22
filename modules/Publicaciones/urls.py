from django.conf.urls import url, include
from .views import Index,Add
urlpatterns = [
    url(r'^$', Index, name='index-publicacion'),
    url(r'^add/$', Add, name='add-publicacion'),

    #Url de ejemplo para viewsets

]
