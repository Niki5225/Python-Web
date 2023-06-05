from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

def validate_name(value):
    if not (65 <= ord(value[0]) <= 90):
        raise ValidationError("Your name must start with a capital letter!")


def validate_plant_name(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Plant name should contain only letters!")


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(2),
        ],
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=20,
        validators=[
            validate_name,
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=20,
        validators=[
            validate_name,
        ],
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Plant(models.Model):
    CHOICES_OF_TYPE_PLANT = (
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants'),
    )

    plant_type = models.CharField(
        max_length=14,
        choices=CHOICES_OF_TYPE_PLANT,
        null=False,
        blank=False,
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=[
            MinLengthValidator(2),
            validate_plant_name,
        ],
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.CharField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk', )
