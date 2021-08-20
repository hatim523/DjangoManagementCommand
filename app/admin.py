from django.contrib import admin

from app.models import DateStore


class DateStoreAdmin(admin.ModelAdmin):
    list_display = ['date_respect_to_timezone', 'timezone']

    def date_respect_to_timezone(self, date_obj: DateStore):
        return f"{date_obj.load_date_with_respective_timezone().strftime('%c')}"


admin.site.register(DateStore, DateStoreAdmin)
