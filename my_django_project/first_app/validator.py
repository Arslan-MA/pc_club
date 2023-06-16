from django.core.validators import *
import datetime


def validator_name(value):
    if not value[0].isupper():
        raise ValidationError("Имя должно быть с заглавной буквы !")


def validator_surname(value):
    if not value[0].isupper():
        raise ValidationError("Фамилия должна быть с заглавной буквы !")
    elif not len(value) < 10:
        raise ValidationError("Не больше 10 символов !")


def validator_age(value):
    if not value > 12:
        raise ValidationError("Вы должны быть старше 12 лет !")


def validator_time(value):
    start = datetime.time(9, 0, 0)
    end = datetime.time(22, 0, 0)
    if start > value or value > end:
        raise ValidationError("Расписание работы клуба (9:00 до 22:00)")


def validator_opinion(value):
    if not len(value) > 10:
        raise ValidationError("Введите больше 10 символов !")


class ValidatorCountry:
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if value % self.base != 0:
            raise ValidationError(f"Не больше {self.base} символов !")
