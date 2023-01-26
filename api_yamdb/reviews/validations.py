import datetime

from django.core.exceptions import ValidationError


def time_validation(year):
    if year > datetime.date.today().year:
        raise ValidationError(
            'Нельзя добавлять произведения, которые еще не вышли.'
        )
    return year
