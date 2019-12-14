from rest_framework import routers

from .views import StateCapitalViewset

router = routers.DefaultRouter()
router.register('api/capitals', StateCapitalViewset, 'capitals')

urlpatterns = router.urls
