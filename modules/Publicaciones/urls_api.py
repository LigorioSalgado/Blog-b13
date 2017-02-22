from django.conf.urls import url,include
from .api_views import PublicacionList,PublicacionDetail
from rest_framework.routers import DefaultRouter
from .api_viewset import PublicacionViewset
router = DefaultRouter()
router.register(r'',PublicacionViewset)
urls = router.urls

urlpatterns = [
    url(r'^$', PublicacionList.as_view(),name='api-list-publicacion'),
    url(r'^(?P<pk>[0-9]+)/$', PublicacionDetail.as_view(),name='api-detail-publicacion'),
#    url(r'^viewsets/',include(router.urls)),
]
