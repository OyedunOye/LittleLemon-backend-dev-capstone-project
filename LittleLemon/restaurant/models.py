from django.db import models

# Create your models here.
class Booking(models.Model):
    # id = models.IntegerField(PrimaryKey=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=1)
    bookingdate = models.DateTimeField()
    
    def __str__(self):
        return self.name + '  ----  ' + str(self.bookingdate)
    

class Menu(models.Model):
    # id = models.IntegerField(PrimaryKey=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title