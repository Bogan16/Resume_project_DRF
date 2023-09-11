from rest_framework import routers
from django.urls import path, include
from .views import ResumeViewSet

router = routers.DefaultRouter()
router.register(r'resumes', ResumeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]