from django.contrib import admin
from django.urls import path, include
from person.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
