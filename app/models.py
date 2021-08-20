from django.db import models

import pytz
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class DateStore(models.Model):
    date = models.DateTimeField()
    timezone = models.CharField(max_length=32, choices=TIMEZONES)

    def load_date_with_respective_timezone(self):
        return self.date.astimezone(pytz.timezone(self.timezone))

    def __str__(self):
        return f"{self.load_date_with_respective_timezone()}"