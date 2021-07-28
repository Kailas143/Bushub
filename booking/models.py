from django.db import models

# Create your models here.


class Bus(models.Model):
    bus_name = models.CharField(max_length=150)
    src = models.CharField(max_length=150)
    dest = models.CharField(max_length=150)
    nos = models.IntegerField()
    rems = models.IntegerField()
    price = models.FloatField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.bus_name

    class Meta:
        verbose_name_plural = 'Buses'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'
    TICKET_STATUS = ((BOOKED, 'BOOKED'), (CANCELLED, 'CANCELLED'))
    email = models.EmailField()
    name = models.CharField(max_length=150)
    userid = models.IntegerField()
    busid = models.IntegerField()
    bus_name = models.CharField(max_length=150)
    source = models.CharField(max_length=150)
    dest = models.CharField(max_length=150)
    nos = models.PositiveIntegerField()
    price = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUS,
                              default=BOOKED,max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bookings'
