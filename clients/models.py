from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=200, null=True, blank=True)
    client_personal_id = models.CharField(max_length=30, null=True, blank=True)
    client_home_tel = models.CharField(max_length=15, null=True, blank=True)
    client_office_tel = models.CharField(max_length=15, null=True, blank=True)
    client_mobile = models.CharField(max_length=25, null=True, blank=True)
    client_address = models.CharField(max_length=500, null=True, blank=True)
    client_province = models.CharField(max_length=200, null=True, blank=True)
    client_nghood = models.CharField(max_length=300, null=True, blank=True)
    client_pobox = models.CharField(max_length=300, null=True, blank=True)
    contact_name = models.CharField(max_length=200, null=True, blank=True)
    contact_id = models.CharField(max_length=30, null=True, blank=True)
    contact_mobile = models.CharField(max_length=25, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='create_client', null=True,
                                   blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='update_client', null=True,
                                   blank=True)
    created_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.client_name
