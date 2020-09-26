from django.core.management.base import BaseCommand


from guest.models import Party


class Command(BaseCommand):
    help = 'create parties from list of invitation code'

    def add_arguments(self, parser):
        parser.add_argument('input', type=str, help='input file')

    def handle(self, *args, **kwargs):
        input_file = kwargs['input']

        code_list = set()
        with open(input_file, "r") as file:
            code_list = set([line.rstrip() for line in file if line.rstrip()])

        party_list = []
        for code in code_list:
            party = Party()
            party.invitation_number = code
            party.name = code
            party_list.append(party)

        Party.objects.bulk_create(party_list)
