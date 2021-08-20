from django.core.management import BaseCommand

from app.management.commands._helpers import create_dummy_user, add_pst_datetimes
from app.models import DateStore

date_object_creation_count = 20


class Command(BaseCommand):
    help = 'Adds dummy users'

    def handle(self, *args, **options):
        self.stdout.write("Creating user...")
        user_obj = create_dummy_user()
        self.stdout.write(f"User: {user_obj.username} created successfully.") if user_obj is not None \
            else self.stdout.write(self.style.ERROR("Could not create user."))

        if DateStore.objects.all().count() >= date_object_creation_count:
            self.stdout.write("Not creating additional datetime objects since the required count already exists")
            return

        self.stdout.write("Creating datetime objects for PST Timezone")
        add_pst_datetimes(date_object_creation_count)
        self.stdout.write(self.style.SUCCESS("PST Timezone datetime objects created!"))



