from rest_framework import serializers
from .models import CustomUser, Trainer, Schedule, Appointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Trainer
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
