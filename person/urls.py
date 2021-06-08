from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    PersonViewSet,
    NewsViewSet,
    TagViewSet
)

router = SimpleRouter()
router.register('person', PersonViewSet)
router.register('news', NewsViewSet)
router.register('tag', TagViewSet)

urlpatterns = [

]
