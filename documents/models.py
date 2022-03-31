from django.contrib.auth.models import User
from django.db import models
from projects.models import Task


# Create your models here.


class Document(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    document_id = models.CharField(max_length=255, null=True, blank=True)
    document_name = models.CharField(max_length=255, null=True, blank=True)
    document_type = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='create_document', null=True,
                                   blank=True)
    create_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='update_document', null=True,
                                   blank=True)

    def __str__(self):
        return self.document_id
