from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, PerformanceViewSet

router = DefaultRouter()
router.register('attendance', AttendanceViewSet)
router.register('performance', PerformanceViewSet)

urlpatterns = router.urls
    