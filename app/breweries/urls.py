from rest_framework import routers

from .views import BreweryViewset

router = routers.DefaultRouter()
router.register('api/breweries', BreweryViewset)

urlpatterns = router.urls
