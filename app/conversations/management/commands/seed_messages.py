from django.core.management import BaseCommand


class Command(BaseCommand):

    help = 'This command create messages!'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            default=2,
            type=int,
            help='How many message want to create?'
        )

    def handle(self, *args, **options):
        number = options.get('number')
