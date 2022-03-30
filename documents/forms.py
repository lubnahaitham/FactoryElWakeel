from django import forms

from documents.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_id', 'document_name', 'document_type', 'created_by']

    labels = {
        'document_id': 'Document ID',
        'document_name': 'Document Name',
        'document_type': 'Document Type',
        'created_by': 'Created By',

    }

