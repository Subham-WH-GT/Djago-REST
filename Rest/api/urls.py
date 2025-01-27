from django.urls import include, path
# import routers
from rest_framework import routers
 
# import everything from views
from .views import *

router= routers.DefaultRouter()

router.register(r'playersapi',PlayerViewSet,basename='playermodel')

urlpatterns=[
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))
]