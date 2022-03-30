from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from clients.models import Client


class Proposal(models.Model):
    PROPOSAL_STATUS = (
        ('Delivered', 'Delivered'),
        ('Executed', 'Executed'),
        ('Pricing', 'Pricing')
    )
    proposal_id = models.CharField(max_length=255, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    proposal_status = models.CharField(max_length=255, choices=PROPOSAL_STATUS, null=True, blank=True)
    proposal_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    proposal_amount = models.FloatField(null=True, blank=True)
    item_type = models.CharField(max_length=255, null=True, blank=True)
    no_items = models.CharField(max_length=255, null=True, blank=True)
    item_details = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to="images/", null=True, blank=True)
    es_width = models.FloatField(null=True, blank=True)
    es_height = models.FloatField(null=True, blank=True)
    fn_width = models.FloatField(null=True, blank=True)
    fn_height = models.FloatField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='create_proposal', null=True,
                                   blank=True)
    created_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='update_proposal', null=True,
                                   blank=True)
    updated_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
