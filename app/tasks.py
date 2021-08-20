from app.management.commands._conversion_helpers import convert_datetime_objects_to_utc, convert_datetime_objects_to_pst

conversion_to_utc = True


class ConversionRoutine:
    def __init__(self, num_dates_to_convert: int = 10):
        self.convert_num_dates = num_dates_to_convert

    def run_routine(self):
        """
        NOTE: This method will be stuck in infinite loop if no DateStore objects are created first
        """
        global conversion_to_utc
        total_converted = 0

        if conversion_to_utc:
            total_converted = convert_datetime_objects_to_utc(self.convert_num_dates)

        if not conversion_to_utc or (conversion_to_utc and total_converted < 1):
            conversion_to_utc = False
            total_converted = convert_datetime_objects_to_pst(self.convert_num_dates)

        if not conversion_to_utc and total_converted < 1:
            conversion_to_utc = True
            self.run_routine()


def run_conversion_routine():
    ConversionRoutine().run_routine()