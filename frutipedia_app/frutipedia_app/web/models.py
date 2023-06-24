from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

def validate_name_if_starts_with_letter(name):
    if not name[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validate_if_name_is_only_letters(name):
    if not name.isalpha():
        raise ValidationError("Fruit name should contain only letters!")


class Profile(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=25,
        validators=[
            MinLengthValidator(2),
            validate_name_if_starts_with_letter,
        ],
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=35,
        validators=[
            MinLengthValidator(1),
            validate_name_if_starts_with_letter,
        ],
    )

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=40,
    )

    password = models.CharField(
        default=None,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(8),
        ],
        max_length=20,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        default=18,
        null=True,
        blank=True,
    )


class Fruit(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=[
            MinLengthValidator(2),
            validate_if_name_is_only_letters,
        ],
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )
