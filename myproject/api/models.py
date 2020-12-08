from django.db import models

# change all nulls to false

class Customer(models.Model):
    customer_id = models.CharField (primary_key=True, max_length=50)
    customer_name = models.CharField(max_length=250)
    phone_number = models.CharField (max_length=50)
    address = models.CharField(max_length=250)
    transport_phases_pick_up = models.ManyToManyField('Transport_Phase', through='Pick_Up', related_name='pu')
    transport_phases_drop_off = models.ManyToManyField('Transport_Phase', through='Drop_Off', related_name='do')

    vehicle_types = models.ManyToManyField('Vehicle_Type', through='Reservation')
    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.customer_id)

class Employee(models.Model):
    employee_id = models.CharField (primary_key=True, max_length=50)
    name = models.CharField(max_length=250)
    sin = models.CharField (max_length=50)
    phone_number = models.CharField (max_length=50)

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.employee_id)

class Delivery_Employee(models.Model):
    e_id = models.OneToOneField(Employee, primary_key=True, on_delete=models.CASCADE)
    license_grade = models.CharField(max_length=50)
    transport_phases = models.ManyToManyField('Transport_Phase', through='Assigned')

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.e_id)

class Manager(models.Model):
    services = models.ManyToManyField('Service', through='Manages')
    e_id = models.OneToOneField(Employee, primary_key=True, on_delete=models.CASCADE)
    office_no = models.IntegerField(unique=True)
    mgr_start_date = models.DateField()

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.office_no)

class Vehicle_Type(models.Model):
    vin = models.CharField (primary_key=True, max_length=50)
    model_year = models.CharField(max_length=50)
    make = models.CharField (max_length=250)
    model = models.CharField(max_length=250)
    customers = models.ManyToManyField('Customer', through='Reservation')

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.vin)

class Rental_Company(models.Model):
    company_name = models.CharField (primary_key=True,max_length=50)
    founded_date = models.DateField()
    head_address = models.CharField (max_length=50)

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.company_name)

class Vehicle(models.Model):
    license_plate = models.CharField (primary_key=True, max_length=250)
    vin = models.ForeignKey(Vehicle_Type, null=False, on_delete=models.CASCADE)
    company_name = models.ForeignKey(Rental_Company, on_delete=models.CASCADE)
    total_no_seats = models.CharField(max_length=50)

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.license_plate)

class Transport_Phase(models.Model):
    date = models.DateField()
    time = models.CharField (max_length=50)
    vin = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    customers_drop_off = models.ManyToManyField('Customer', through='Drop_Off', related_name='do')
    customers_pick_up = models.ManyToManyField('Customer', through='Pick_Up', related_name='pu')
    delivery_employees = models.ManyToManyField('Delivery_Employee', through='Assigned')

    class Meta:
        unique_together=('date', 'time', 'vin')
        app_label='api'

    def __str__(self):
        return str(self.date)


class Payment(models.Model):
    customer_id = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    start_date = models.DateField(null=False) # change to False
    end_date = models.DateField(null=False) # change to False
    rate = models.FloatField()
    total_price = models.FloatField()
    company_name = models.ForeignKey(Rental_Company, null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("customer_id", "start_date", "end_date", "company_name")
        app_label='api'

    def __str__(self):
        return str(self.company_name)

class Service(models.Model):
    managers = models.ManyToManyField('Manager', through='Manages')
    hours = models.CharField (max_length=50)
    date = models.DateField()
    workcode = models.CharField (max_length=50)
    license_plate = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        unique_together=('date', 'workcode', 'license_plate')
        app_label='api'

    def __str__(self):
        return self.date, self.workcode, self.license_plate

class Assigned(models.Model):
    transport_phase = models.ForeignKey(Transport_Phase, on_delete=models.CASCADE)
    delivery_employee = models.ForeignKey(Delivery_Employee, on_delete=models.CASCADE)
    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.delivery_employee.e_id)

class Drop_Off(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transport_phase = models.ForeignKey(Transport_Phase, on_delete=models.CASCADE)
    drop_location = models.CharField (max_length=250)
    drop_time = models.CharField (max_length=50)

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.customer.customer_id)

class Manages(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.m_id)

class Pick_Up(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transport_phase = models.ForeignKey(Transport_Phase, on_delete=models.CASCADE)
    pick_location = models.CharField (max_length=250)
    pick_time = models.CharField (max_length=50)

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.customer.customer_id)

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    reservation_date = models.DateField()

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.customer_id)
