from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token
#from django.conf.urls.static import static


urlpatterns = [
    url(r'^users/', include('modules.Usuarios.urls_api')),
    url(r'^publicaciones/', include('modules.Publicaciones.urls_api')),
    url(r'^auth/', obtain_jwt_token),
    #TODO agregar publicaciones
]
