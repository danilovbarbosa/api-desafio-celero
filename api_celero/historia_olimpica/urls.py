from rest_framework.routers import DefaultRouter, SimpleRouter

from historia_olimpica.views import NocRegionsViewSet, AthleteEventsViewSet

router = SimpleRouter()
router.register(r'athlete_events', AthleteEventsViewSet, basename='athlete_events')
router.register(r'noc_regions', NocRegionsViewSet, basename='noc_regions')


historia_olimpica_urls = router.urls