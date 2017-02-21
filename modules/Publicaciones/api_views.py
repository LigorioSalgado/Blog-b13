from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Publicacion
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser,AllowAny
from .permissions import GroupPermission,OnlyGetPermission
import django_filters.rest_framework

class PublicacionList(generics.ListCreateAPIView):

    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    filter_backends =  (filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('nombre','fecha','tags')
    search_fields = ('nombre','fecha','tags')



    '''
    def get_queryset(self):

        queryset = Publicacion.objects.all()
        name = self.request.query_params.get('publicacion',None)
        if name  is not None:
            queryset = Publicacion.objects.filter(nombre__icontains=name)

        return queryset
        '''
class PublicacionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
