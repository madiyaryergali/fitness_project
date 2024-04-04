from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fitness_schedule.views import UserViewSet, TrainerViewSet, ScheduleViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
