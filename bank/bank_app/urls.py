from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomerDetail, AccountViewSet, ActionViewSet

router = DefaultRouter()

router.register('customer', CustomerDetail)
router.register('account', AccountViewSet)
router.register('action', ActionViewSet)

urlpatterns = [
    path('', include(router.urls))
]