from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.

def validate_if_username_isalphanumeric(value):
    for character in value:
        if not character.isalnum() and character != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            validate_if_username_isalphanumeric,
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    GENRE_CHOICES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    )
    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30,
    )

    artist = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=GENRE_CHOICES,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(0.0),),
    )

    class Meta:
        ordering = ('pk', )