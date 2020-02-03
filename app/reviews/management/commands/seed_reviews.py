import random

from django.core.management import BaseCommand
from django_seed import Seed

from reviews import models as reviews_models
from users import models as users_models
from rooms import models as rooms_models

class Command(BaseCommand):
    help = 'This commnad create reviews!'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            default=2,
            type=int,
            help='How many review want to create?'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        users = users_models.User.objects.all()
        rooms = rooms_models.Room.objects.all()
        seeder = Seed.seeder()

        seeder.add_entity(
            reviews_models.Review,
            number,
            {
                'accuracy': lambda x: random.randint(0, 5),
                'communication': lambda x: random.randint(0, 5),
                'cleanliness': lambda x: random.randint(0, 5),
                'location': lambda x: random.randint(0, 5),
                'check_in': lambda x: random.randint(0, 5),
                'value': lambda x: random.randint(0, 5),
                'user': lambda x: random.choice(users),
                'room': lambda x: random.choice(rooms),

            }
        )

        seeder.execute()

        return self.stdout.write(self.style.SUCCESS(f'{number} review create!'))
