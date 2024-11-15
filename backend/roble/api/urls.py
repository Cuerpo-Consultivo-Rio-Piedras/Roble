from rest_framework import routers
from django.urls import path, include


from api.views.landuse import LandUseViewSet
from api.views.transmission import TransmissionLineViewSet
from api.views.street import StreetSegmentViewSet

router = routers.DefaultRouter()
router.register(r'landuse', LandUseViewSet)
router.register(r'transmission_line', TransmissionLineViewSet)
router.register(r'street', StreetSegmentViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]