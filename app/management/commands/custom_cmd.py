from django.core.management import BaseCommand

from app.management.commands._helpers import create_dummy_user


class Command(BaseCommand):
    help = 'Adds dummy users'

    def handle(self, *args, **options):
        self.stdout.write("Creating user...")
        user_obj = create_dummy_user()
        self.stdout.write(f"User: {user_obj.username} created successfully.") if user_obj is not None \
            else self.stdout.write(self.style.ERROR("Could not create user."))



