import json
from django.core.management.base import BaseCommand, CommandError
from budgest.models import Ambito


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=file)

    def handle(self, *args, **options):
        try:
            ambiti_json = json.load(options['file'])
        except:
            raise CommandError('Parametro "file" non corretto')
        for ambito_json in ambiti_json:
            a = Ambito(
                num=ambito_json['num'],
                descrizione=ambito_json['descrizione'],
                is_active=ambito_json['is_active'],
            )
            a.save()
        self.stdout.write('Importazione ambiti completata con successo')
