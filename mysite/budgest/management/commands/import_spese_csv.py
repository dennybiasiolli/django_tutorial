# -*- coding: utf-8 -*-
import csv, datetime
from django.core.management.base import BaseCommand, CommandError
from budgest.models import Ambito, Spesa, Tag


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=file)

    def handle(self, *args, **options):
        try:
            spese_csv = csv.reader(options['file'])
        except:
            raise CommandError('Parametro "file" non corretto')
        for spesa_csv in spese_csv:
            s = Spesa(
                importo=spesa_csv[1].replace('€', '').replace(' ', '').replace('.', '').replace(',', '.'),
                descrizione=spesa_csv[2],
                quantita=spesa_csv[3],
            )
            data_val = datetime.datetime.strptime(spesa_csv[0], '%d/%m/%Y')
            s.data_accredito = data_val
            s.data_riferimento = data_val
            # lettura ambito e abbinamento all'oggetto
            ambiti = Ambito.objects.filter(num__exact=spesa_csv[4])
            if not ambiti:
                raise CommandError('Non esiste l\'Ambito_ID=%d' % spesa_csv[4])
                exit()
            s.ambito = ambiti[0]
            # lettura tags e abbinamento
            s.save()
            elenco_tags = spesa_csv[6].replace(' ', '')
            if len(elenco_tags) > 0:
                for tag in elenco_tags.split(','):
                    t, created = Tag.objects.get_or_create(descrizione=tag)
                    s.tags.add(t)
                s.save()
        self.stdout.write('Importazione spese completata con successo')
