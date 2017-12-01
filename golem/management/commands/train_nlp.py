from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Trains the NLP for text entity extraction'

    def add_arguments(self, parser):
        parser.add_argument('entity', nargs='+', type=str)

    def handle(self, *args, **options):
        from golem.nlp import train
        if options.get('entity'):
            train.train_all(options['entity'])
        else:
            train.train_all()