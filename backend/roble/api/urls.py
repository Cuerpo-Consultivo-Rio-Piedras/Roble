from rest_framework import routers
from django.urls import path, include


from .views import PoiViewSet

router = routers.DefaultRouter()
router.register(r'poi', PoiViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]