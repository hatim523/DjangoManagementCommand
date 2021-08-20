import pytz
from django.contrib.auth.models import User
import random
import datetime

from django.utils import timezone

pst_timezone = pytz.timezone(zone='US/Pacific')
utc_timezone = pytz.timezone(zone='UTC')


def check_if_username_exists(username):
    return User.objects.filter(username=username).exists()


def create_dummy_user():
    try:
        while True:
            random_digits = "".join([str(random.randint(0, 9)) for i in range(random.randint(1, 10))])
            username = "hatim" + random_digits
            if not check_if_username_exists(username):
                break

        user_obj = User.objects.create(
            username=username,
            first_name='Hatim',
        )

        user_obj.set_password("helloworld123")
        user_obj.save()
        return user_obj
    except Exception as e:
        print(e)
        return None


def create_pst_datetime():
    # initializing random integers to create random datetime object
    random_year = random.randint(1990, 2050)
    random_month = random.randint(1, 12)
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)

    random_date = datetime.datetime(year=random_year, month=random_month, day=1, hour=random_hour, minute=random_minute)

    # now making naive datetime aware (PST Timezone)
    return pst_timezone.localize(random_date)


def convert_pst_datetime_to_utc(pst_datetime: datetime.datetime) -> datetime.datetime:
    # check if datetime is of pst zone, if not then return as is
    if pst_datetime.tzinfo.zone != 'US/Pacific':
        return pst_datetime
    
    return pst_datetime.astimezone(utc_timezone)