import json
from django.core.management.base import BaseCommand, CommandError
from budgest.models import Ambito, Spesa, Tag


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=file)

    def handle(self, *args, **options):
        try:
            spese_json = json.load(options['file'])
        except:
            raise CommandError('Parametro "file" non corretto')
        for spesa_json in spese_json:
            s = Spesa(
                importo=spesa_json['Importo'],
                descrizione=spesa_json['Descrizione'],
                quantita=spesa_json['Quantita'],
            )
            data_val = spesa_json['Data']
            s.data_accredito = data_val
            s.data_riferimento = data_val
            # lettura ambito e abbinamento all'oggetto
            ambiti = Ambito.objects.filter(num__exact=spesa_json['Ambito_ID'])
            if not ambiti:
                raise CommandError('Non esiste l\'Ambito_ID=%d' % spesa_json['Ambito_ID'])
                exit()
            s.ambito = ambiti[0]
            # lettura tags e abbinamento
            s.save()
            elenco_tags = spesa_json['Tags'].replace(' ', '')
            if len(elenco_tags) > 0:
                for tag in elenco_tags.split(','):
                    t, created = Tag.objects.get_or_create(descrizione=tag)
                    s.tags.add(t)
                s.save()
        self.stdout.write('Importazione spese completata con successo')
