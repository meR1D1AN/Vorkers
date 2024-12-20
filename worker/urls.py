from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *
from .apps import WorkersConfig

app_name = WorkersConfig.name

router = DefaultRouter()
router.register(r"workers", WorkerViewSet, basename="worker")

urlpatterns = [
    path("", include(router.urls)),
    path('team/<int:team_id>/workers/', WorkerViewSet.as_view({'get': 'team_list'}), name='team-worker-list'),
]
