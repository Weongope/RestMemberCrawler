from django.urls import include, path
from rest_framework import routers
from restmember import views
from django.contrib import admin
#from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'list', views.listViewSet, 'list' )
router.register(r'search', views.searchViewSet, 'search')
router.register(r'mp', views.mpViewSet, 'mp')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
