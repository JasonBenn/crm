import os

import throttle
from pgvector.django import L2Distance
from pyairtable import Table

from crm import settings
from interests.models import AirtablePersons, Interests


@throttle.wrap(1, 5)
def fetch_airtable_people():
    # find all people in an airtable table
    table = Table(os.environ['AIRTABLE_API_KEY'], os.environ['AIRTABLE_BASE_ID'], 'People')
    people = table.all()
    airtable_people = []
    for person in people:
        airtable_person = AirtablePersons(
            airtable_id=person['id'],
            first_name=person['fields']['First name'],
            last_name=person['fields']['Last name'],
            twitter=person['fields'].get('Twitter', None),
            facebook=person['fields'].get('Facebook', None),
            linkedin=person['fields'].get('LinkedIn', None)
        )

        airtable_people.append(airtable_person)
    AirtablePersons.objects.bulk_create(airtable_people, update_conflicts=True, update_fields=['first_name', 'last_name', 'twitter', 'facebook', 'linkedin'], unique_fields=['airtable_id'])
    print(f"Fetched {len(airtable_people)} people from Airtable")


def generate_list_of_social_links_to_check():
    pass


def invoke_scrapers():
    pass


def process_raw_contents():
    pass


def extract_interests():
    pass


def embed_interests():
    pass


def query_related_interests(query):
    return Interests.objects.order_by(L2Distance('embedding', query))[:10]
