from rest_framework.routers import DefaultRouter

from historia_olimpica.views import NocRegionsViewSet, AthleteEventsViewSet

router = DefaultRouter()
router.register(r'', NocRegionsViewSet, basename='noc_regions')
router.register(r'', AthleteEventsViewSet, basename='athlete_events')

historia_olimpica_urls = router.urls