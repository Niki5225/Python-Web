from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


# Create your models here.

def validate_username(value):
    if len(value) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")


def validate_year(value):
    if not (1980 <= value <= 2049):
        raise ValidationError("Year must be between 1980 and 2049")


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[
            validate_username,
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(18),
        ],
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    CAR_TYPE_CHOICES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )

    car_type = models.CharField(
        null=False,
        blank=False,
        choices=CAR_TYPE_CHOICES,
        max_length=10,
    )

    car_model = models.CharField(
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2),
        ],
        max_length=20,
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            validate_year,
        ],
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1),
        ]
    )
