from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet


router = DefaultRouter()
router.register(r'', LinkViewSet)
router.register(r'<str: key>', LinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
