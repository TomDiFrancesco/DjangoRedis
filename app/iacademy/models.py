import json
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse
from .utils import send_transaction, get_transaction_by_hash, certificate_to_dictionary
import hashlib
import codecs
from app import settings



class Certificate(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    grade = models.IntegerField()
    subject = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_creation = models.DateField(default=timezone.localdate())
    transaction_id = models.TextField(null=True, blank=True, editable=False)

    def save(self):
        self.transaction_id = self.write_on_chain()
        super(Certificate, self).save()

    def write_on_chain(self):
        dictionary = certificate_to_dictionary(self)
        return send_transaction(message=json.dumps(dictionary),
                                              address_to='0x0000000000000000000000000000000000000000',
                                              address_from='0x00583328725E92B2e9E45a0c96058c533B6aB76d',
                                              private_key='0x0bd7acb0531d3cb2d4595475b3ef5f9027c4c1f0420e591cb2c1a0243c4b6a79',
                                              amount=0)

    def get_absolute_url(self):
        return reverse('certificate-detail', args=[self.id])