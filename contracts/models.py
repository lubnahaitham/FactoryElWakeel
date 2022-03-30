from django.contrib.auth.models import User
from django.db import models
from proposals.models import Proposal


# Create your models here.

class Contract(models.Model):
    CONTRACT_STATUS = (
        ('A', 'A'),
        ('B', 'B'),
    )
    contract_id = models.CharField(max_length=255, null=True, blank=True)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name='proposal_contract',
                                 null=True, blank=True)
    contract_status = models.CharField(max_length=255, choices=CONTRACT_STATUS, null=True, blank=True)
    item_type = models.CharField(max_length=255, null=True, blank=True)
    no_items = models.CharField(max_length=255, null=True, blank=True)
    item_details = models.CharField(max_length=255, null=True, blank=True)
    fn_width = models.FloatField(null=True, blank=True)
    fn_height = models.FloatField(null=True, blank=True)
    img = models.ImageField(upload_to="images/", null=True, blank=True)
    contract_start_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    contract_delivery_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='create_contract', null=True,
                                   blank=True)
    created_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='update_contract', null=True,
                                   blank=True)
    updated_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.contract_id
