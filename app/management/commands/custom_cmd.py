from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Adds dummy users'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("HOOOO!"))