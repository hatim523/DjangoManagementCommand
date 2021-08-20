import datetime

import pytz

from app.management.commands._helpers import load_date_with_timezone_info
from app.models import DateStore


def datestore_object_generator():
    objects = DateStore.objects.all()
    for obj in objects:
        yield obj


def convert_datetime_objects_to_utc(count: int) -> int:
    """
    Parameters:
        count: Number of objects to convert
    Returns number of converted datetime objects
    """
    return convert_datetime_objects_to_given_timezone(count, pytz.timezone(zone='UTC'))


def convert_datetime_objects_to_pst(count: int) -> int:
    """
    Parameters:
        count: Number of objects to convert
    Returns number of converted datetime objects
    """
    return convert_datetime_objects_to_given_timezone(count, pytz.timezone(zone='US/Pacific'))


def convert_datetime_objects_to_given_timezone(count: int, to_timezone: pytz.timezone) -> int:
    datestore_iterator = datestore_object_generator()
    converted_objects = 0

    for date_obj in datestore_iterator:
        date = date_obj.load_date_with_respective_timezone()
        status, mod_date = convert_datetime_object(date, to_timezone)
        if status:
            converted_objects += 1

            # saving modified date
            # date_obj.date = mod_date
            date_obj.timezone = mod_date.tzinfo.zone
            date_obj.save()

        # check if count is satisfied
        if converted_objects >= count:
            break

    return converted_objects


def convert_datetime_object(date: datetime.datetime, to_timezone: pytz.timezone) -> tuple:
    """
    Returns:
        (True, datetime.datetime) if datetime object was converted to given timezone
        (False, datetime.datetime) if datetime object was already in the given timezone
    """
    if date.tzinfo.zone == to_timezone.zone:
        return False, date

    return True, date.astimezone(to_timezone)