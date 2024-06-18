from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("blogs",views.PostModelViewSet)
urlpatterns=[
    path("",include(router.urls))
]