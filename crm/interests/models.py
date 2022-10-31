from django.db import models
from pgvector.django import VectorField


class AirtablePersons(models.Model):
    airtable_id = models.CharField(max_length=255, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    twitter = models.TextField(null=True)
    facebook = models.TextField(null=True)
    linkedin = models.TextField(null=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class RawContents(models.Model):
    airtable_person = models.ForeignKey(AirtablePersons, on_delete=models.CASCADE)
    url = models.TextField()
    content = models.TextField()
    last_scraped = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[0:20] + "..."


class ProcessedContents(models.Model):
    raw_content = models.ForeignKey(RawContents, on_delete=models.CASCADE)
    content = models.TextField()
    last_processed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[0:20] + "..."


class Interests(models.Model):
    # indexes = [
    #     IvfflatIndex(
    #         name='embedding_index',
    #         fields=['embedding'],
    #         lists=100,
    #         opclasses=['vector_l2_ops']
    #     )
    # ]

    processed_content = models.ForeignKey(ProcessedContents, on_delete=models.CASCADE)
    interest = models.CharField(max_length=255, unique=True)
    embedding = VectorField(dimensions=1024, null=True)

    def __str__(self):
        return self.interest
