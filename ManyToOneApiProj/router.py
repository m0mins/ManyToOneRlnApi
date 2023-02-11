from carapp.viewsets import CarSpecsViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('car',CarSpecsViewset)