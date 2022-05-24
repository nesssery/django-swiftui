from django.urls import path, include
from swiftui import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'banks', views.BankViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls')),
]