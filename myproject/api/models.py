from django.db import models

# change all nulls to false

class Customer(models.Model):
    customer_id = models.CharField (primary_key=True, default="id",max_length=50)
    customer_name = models.CharField(max_length=250)
    phone_number = models.CharField (max_length=50)
    address = models.CharField(max_length=250)

    class Meta:
        app_label='api'

    def __str__(self):
        return self.customer_id

class Employee(models.Model):
    employee_id = models.CharField (primary_key=True, max_length=50)
    name = models.CharField(max_length=250)
    sin = models.CharField (max_length=50)
    phone_number = models.CharField (max_length=50)

    class Meta:
        app_label='api'

    def __str__(self):
        return self.employee_id

class Delivery_Employee(models.Model):
    e_id = models.OneToOneField(Employee, primary_key=True, on_delete=models.CASCADE)
    license_grade = models.CharField(max_length=50)

    class Meta:
        app_label='api'

    def __str__(self):
        return self.e_id

class Manager(models.Model):
    e_id = models.OneToOneField(Employee, primary_key=True, default="id", on_delete=models.CASCADE)
    office_no = models.IntegerField()
    mgr_start_date = models.CharField(max_length=250)

    class Meta:
        app_label='api'

    def __str__(self):
        return self.e_id

class Vehicle_Type(models.Model):
    vin = models.CharField (primary_key=True, default="vin",max_length=50)
    model_year = models.CharField(max_length=50)
    make = models.CharField (max_length=250)
    model = models.CharField(max_length=250)

    class Meta:
        app_label='api'

    def __str__(self):
        return self.vin

class Rental_Company(models.Model):
    company_name = models.CharField (primary_key=True, default="id",max_length=50)
    founded_date = models.DateField()
    head_address = models.CharField (max_length=50)

    class Meta:
        app_label='api'

    def __str__(self):
        return self.company_name

class Vehicle(models.Model):
    license_plate = models.CharField (primary_key=True, default="plate", max_length=250)
    vin = models.ForeignKey(Vehicle_Type, null=False, default='vin', on_delete=models.CASCADE)
    company_name = models.ForeignKey(Rental_Company, on_delete=models.CASCADE)
    total_no_seats = models.CharField(max_length=50)

    class Meta:
        app_label='api'

    def __str__(self):
        return self.license_plate

class Transport_Phase(models.Model):
    date = models.DateField()
    time = models.CharField (max_length=50)
    vin = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)

    class Meta:
        unique_together=('date', 'time', 'vin')
        app_label='api'

    def __str__(self):
        return self.date, self.time, self.vin


class Payment(models.Model):
    customer_id = models.ForeignKey(Customer, null=False, default='id', on_delete=models.CASCADE)
    start_date = models.DateField(null=False) # change to False
    end_date = models.DateField(null=False) # change to False
    rate = models.FloatField()
    total_price = models.FloatField()
    company_name = models.ForeignKey(Rental_Company, null=False, default='name', on_delete=models.CASCADE)

    class Meta:
        unique_together = ("customer_id", "start_date", "end_date", "company_name")
        app_label='api'

    def __str__(self):
        return self.company_name

class Service(models.Model):
    hours = models.CharField (max_length=50)
    date = models.DateField()
    workcode = models.CharField (max_length=50)
    license_plate = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        unique_together=('date', 'workcode', 'license_plate')
        app_label='api'

    def __str__(self):
        return self.date, self.workcode, self.license_plate

# change null to False
class Assigned(models.Model):
    date = models.ForeignKey(Transport_Phase, null=False, on_delete=models.CASCADE, related_name='as_date') 
    time = models.ForeignKey(Transport_Phase, null=False, on_delete=models.CASCADE, related_name='as_time')
    vin = models.ForeignKey(Transport_Phase, null=False, on_delete=models.CASCADE, related_name='as_vin')
    d_id = models.ForeignKey(Delivery_Employee, null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together=('date', 'time', 'vin', 'd_id')
        app_label='api'

    def __str__(self):
        return self.date, self.time, self.vin, self.d_id

# change null to False
class Drop_Off(models.Model):
    date = models.ForeignKey(Transport_Phase, null=False, on_delete=models.CASCADE, related_name='do_date')
    time = models.ForeignKey(Transport_Phase, null=False, on_delete=models.CASCADE, related_name='do_time')
    vin = models.ForeignKey(Transport_Phase, null=False, on_delete=models.CASCADE, related_name='do_vin')
    c_id = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    drop_location = models.CharField (max_length=250)
    drop_time = models.CharField (max_length=50)

    class Meta:
        unique_together=('date', 'time', 'vin', 'c_id')
        app_label='api'

    def __str__(self):
        return self.date, self.time, self.vin, self.c_id

# change null to False
class Manages(models.Model):
    m_id = models.ForeignKey(Manager, null=False, on_delete=models.CASCADE)
    license_plate = models.ForeignKey(Service, null=False, on_delete=models.CASCADE)
    date = models.ForeignKey(Service, null=False, on_delete=models.CASCADE, related_name='m_date')
    workcode = models.ForeignKey(Service, null=False, on_delete=models.CASCADE, related_name='m_workcode')

    class Meta:
        unique_together = ("m_id", "license_plate", "date", "workcode")
        app_label='api'

    def __str__(self):
        return self.m_id, self.license_plate, self.date, self.workcode

class Pick_Up(models.Model):
    date = models.ForeignKey(Transport_Phase, null=False, on_delete=models.CASCADE, related_name='pu_date')
    time = models.ForeignKey(Transport_Phase, null=False, on_delete=models.CASCADE, related_name='pu_time')
    vin = models.ForeignKey(Transport_Phase, null=False, on_delete=models.CASCADE, related_name='pu_vin')
    c_id = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    pick_location = models.CharField (max_length=250)
    pick_time = models.CharField (max_length=50)

    class Meta:
        unique_together=('date', 'time', 'vin', 'c_id')
        app_label='api'

    def __str__(self):
        return self.date, self.time, self.vin, self.c_id

class Reservation(models.Model):
    customer_id = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    vin = models.ForeignKey(Vehicle_Type, null=False, on_delete=models.CASCADE)
    reservation_date = models.DateField()

    class Meta:
        unique_together=('customer_id', 'vin')
        app_label='api'

    def __str__(self):
        return self.customer_id, self.vin
