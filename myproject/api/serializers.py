from rest_framework import serializers
from . import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class Delivery_EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Delivery_Employee
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manager
        fields = '__all__'

class Vehicle_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle_Type
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = '__all__'

class Transport_PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transport_Phase
        fields = '__all__'

class Rental_CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rental_Company
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'

class AssignedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assigned
        fields = '__all__'

class Drop_OffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drop_Off
        fields = '__all__'

class ManagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manages
        fields = '__all__'

class Pick_UpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pick_Up
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = '__all__'
