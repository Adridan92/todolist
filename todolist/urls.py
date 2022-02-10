
from django.urls import include, path
from rest_framework.routers import DefaultRouter

# Views
from todolist.services.views import TaskViewSet
from .views import home

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, base_name='tasks')

urlpatterns = [
    path('home/',home, name='home'),
    path('', include(router.urls))
]
