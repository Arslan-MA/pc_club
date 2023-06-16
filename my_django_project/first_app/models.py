from django.db import models
from first_app.validator import *
import datetime


class Visitor(models.Model):
    name = models.CharField(max_length=50, validators=[validator_name])
    surname = models.CharField(max_length=50, validators=[validator_surname])
    age = models.IntegerField(validators=[validator_age])

    GENDER = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
    )

    gender = models.CharField(max_length=30, choices=GENDER)
    work_status = models.CharField(max_length=60)
    favorite_genre = models.CharField(max_length=80)
    visiting_time = models.TimeField(validators=[validator_time])

    PLATFORM = (
        ('PC', 'PC'),
        ('XBOX', 'XBOX'),
        ('Playstation', 'Playstation')
    )

    favorite_platform = models.CharField(max_length=80, choices=PLATFORM)
    n = 100
    country = models.CharField(max_length=80)
    opinion = models.TextField(validators=[validator_opinion])

    def __str__(self):
        return f"{self.name} - {self.surname}"
