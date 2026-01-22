from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]

    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name='car_models'
    )

    dealer_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
