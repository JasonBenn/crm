from django.core.management.base import BaseCommand

from interests.pipeline import fetch_airtable_people


class Command(BaseCommand):

    def handle(self, *args, **options):
        fetch_airtable_people()