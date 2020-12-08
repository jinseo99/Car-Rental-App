from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class CustomerList (APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer (customers, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail (APIView):
    def get(self, request, pk, format=None):
        customer = Customer.objects.get (pk=pk)
        serializer = CustomerSerializer(customer)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        customer = Customer.objects.filter(pk=pk).first()
        serializer = CustomerSerializer(customer, data=request.data)
        print(customer)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = Customer.objects.filter (pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeList (APIView):
    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer (employees, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail (APIView):
    def get(self, request, pk, format=None):
        employee = Employee.objects.get (pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        employee = Employee.objects.filter(pk=pk).first()
        serializer = EmployeeSerializer(employee, data=request.data)
        print(employee)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = Employee.objects.filter (pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Delivery_EmployeeList (APIView):
    def get(self, request, format=None):
        delivery_employees = Delivery_Employee.objects.all()
        serializer = Delivery_EmployeeSerializer (delivery_employees, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = Delivery_EmployeeSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Delivery_EmployeeDetail (APIView):

    def get(self, request, pk, format=None):
        delivery_employee = Delivery_Employee.objects.get (pk=pk)
        serializer = Delivery_EmployeeSerializer(delivery_employee)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        delivery_employee = Delivery_Employee.objects.filter(pk=pk).first()
        serializer = Delivery_EmployeeSerializer(delivery_employee, data=request.data)
        print(delivery_employee)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        delivery_employee = Delivery_Employee.objects.filter (pk=pk)
        delivery_employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ManagerList (APIView):
    def get(self, request, format=None):
        managers = Manager.objects.all()
        serializer = ManagerSerializer (managers, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = ManagerSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagerDetail (APIView):

    def get(self, request, pk, format=None):
        manager = Manager.objects.get (pk=pk)
        serializer = ManagerSerializer(manager)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        manager = Manager.objects.filter(pk=pk).first()
        serializer = ManagerSerializer(manager, data=request.data)
        print(manager)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        manager = Manager.objects.filter (pk=pk)
        manager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Vehicle_TypeList (APIView):
    def get(self, request, format=None):
        vehicle_types = Vehicle_Type.objects.all()
        serializer = Vehicle_TypeSerializer (vehicle_types, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = Vehicle_TypeSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Vehicle_TypeDetail (APIView):

    def get(self, request, pk, format=None):
        vehicle_type = Vehicle_Type.objects.get (pk=pk)
        serializer = Vehicle_TypeSerializer(vehicle_type)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        vehicle_type = Vehicle_Type.objects.filter(pk=pk).first()
        serializer = Vehicle_TypeSerializer(vehicle_type, data=request.data)
        print(vehicle_type)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vehicle_type = Vehicle_Type.objects.filter (pk=pk)
        vehicle_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VehicleList (APIView):
    def get(self, request, format=None):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer (vehicles, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = VehicleSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleDetail (APIView):

    def get(self, request, pk, format=None):
        vehicle = Vehicle.objects.get (pk=pk)
        serializer = VehicleSerializer(vehicle)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        vehicle = Vehicle.objects.filter(pk=pk).first()
        serializer = VehicleSerializer(vehicle, data=request.data)
        print(vehicle)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vehicle = Vehicle.objects.filter (pk=pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Transport_PhaseList (APIView):
    def get(self, request, format=None):
        transport_phases = Transport_Phase.objects.all()
        serializer = Transport_PhaseSerializer (transport_phases, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = Transport_PhaseSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Transport_PhaseDetail (APIView):

    def get(self, request, pk, format=None):
        transport_phase = Transport_Phase.objects.get (pk=pk)
        serializer = Transport_PhaseSerializer(transport_phase)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        transport_phase = Transport_Phase.objects.filter(pk=pk).first()
        serializer = Transport_PhaseSerializer(transport_phase, data=request.data)
        print(transport_phase)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        transport_phase = Transport_Phase.objects.filter (pk=pk)
        transport_phase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Rental_CompanyList (APIView):
    def get(self, request, format=None):
        rental_companys = Rental_Company.objects.all()
        serializer = Rental_CompanySerializer (rental_companys, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = Rental_CompanySerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Rental_CompanyDetail (APIView):

    def get(self, request, pk, format=None):
        rental_company = Rental_Company.objects.get (pk=pk)
        serializer = Rental_CompanySerializer(rental_company)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        rental_company = Rental_Company.objects.filter(pk=pk).first()
        serializer = Rental_CompanySerializer(rental_company, data=request.data)
        print(rental_company)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rental_company = Rental_Company.objects.filter (pk=pk)
        rental_company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PaymentList (APIView):
    def get(self, request, format=None):
        payments = Payment.objects.all()
        serializer = PaymentSerializer (payments, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = PaymentSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetail (APIView):

    def get(self, request, pk, format=None):
        payment = Payment.objects.get (pk=pk)
        serializer = PaymentSerializer(payment)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        payment = Payment.objects.filter(pk=pk).first()
        serializer = PaymentSerializer(payment, data=request.data)
        print(payment)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        payment = Payment.objects.filter (pk=pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ServiceList (APIView):
    def get(self, request, format=None):
        services = Service.objects.all()
        serializer = ServiceSerializer (services, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = ServiceSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceDetail (APIView):

    def get(self, request, pk, format=None):
        service = Service.objects.get (pk=pk)
        serializer = ServiceSerializer(service)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        service = Service.objects.filter(pk=pk).first()
        serializer = ServiceSerializer(service, data=request.data)
        print(service)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        service = Service.objects.filter (pk=pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AssignedList (APIView):
    def get(self, request, format=None):
        assigneds = Assigned.objects.all()
        serializer = AssignedSerializer (assigneds, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = AssignedSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssignedDetail (APIView):

    def get(self, request, pk, format=None):
        assigned = Assigned.objects.get (pk=pk)
        serializer = AssignedSerializer(assigned)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        assigned = Assigned.objects.filter(pk=pk).first()
        serializer = AssignedSerializer(assigned, data=request.data)
        print(assigned)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        assigned = Assigned.objects.filter (pk=pk)
        assigned.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Drop_OffList (APIView):
    def get(self, request, format=None):
        drop_offs = Drop_Off.objects.all()
        serializer = Drop_OffSerializer (drop_offs, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = Drop_OffSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Drop_OffDetail (APIView):

    def get(self, request, pk, format=None):
        drop_off = Drop_Off.objects.get (pk=pk)
        serializer = Drop_OffSerializer(drop_off)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        drop_off = Drop_Off.objects.filter(pk=pk).first()
        serializer = Drop_OffSerializer(drop_off, data=request.data)
        print(drop_off)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        drop_off = Drop_Off.objects.filter (pk=pk)
        drop_off.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ManagesList (APIView):
    def get(self, request, format=None):
        managess = Manages.objects.all()
        serializer = ManagesSerializer (managess, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = ManagesSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagesDetail (APIView):

    def get(self, request, pk, format=None):
        manages = Manages.objects.get (pk=pk)
        serializer = ManagesSerializer(manages)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        manages = Manages.objects.filter(pk=pk).first()
        serializer = ManagesSerializer(manages, data=request.data)
        print(manages)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        manages = Manages.objects.filter (pk=pk)
        manages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Pick_UpList (APIView):
    def get(self, request, format=None):
        pick_ups = Pick_Up.objects.all()
        serializer = Pick_UpSerializer (pick_ups, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = Pick_UpSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Pick_UpDetail (APIView):

    def get(self, request, pk, format=None):
        pick_up = Pick_Up.objects.get (pk=pk)
        serializer = Pick_UpSerializer(pick_up)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        pick_up = Pick_Up.objects.filter(pk=pk).first()
        serializer = Pick_UpSerializer(pick_up, data=request.data)
        print(pick_up)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pick_up = Pick_Up.objects.filter (pk=pk)
        pick_up.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReservationList (APIView):
    def get(self, request, format=None):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer (reservations, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationDetail (APIView):

    def get(self, request, pk, format=None):
        reservation = Reservation.objects.get (pk=pk)
        serializer = ReservationSerializer(reservation)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        reservation = Reservation.objects.filter(pk=pk).first()
        serializer = ReservationSerializer(reservation, data=request.data)
        print(reservation)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reservation = Reservation.objects.filter (pk=pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)