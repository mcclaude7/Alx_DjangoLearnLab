from .views import CohortViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cohorts', CohortViewSet, basename='cohort')

urlpatterns = router.urls