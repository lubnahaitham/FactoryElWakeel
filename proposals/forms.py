from django import forms
from django.core import validators
from .models import Proposal


class ProposalForm(forms.ModelForm):
    proposal_id = forms.CharField(validators=[validators.MinLengthValidator(4)])

    class Meta:
        model = Proposal
        fields = ['proposal_id', 'proposal_status',
                  'proposal_amount', 'item_type', 'no_items',
                  'item_details', 'img', 'es_width', 'es_height', 'fn_width', 'fn_height',
                  'created_by', 'created_date', 'updated_by', 'updated_date']
        # widgets = {
        #     'item_type': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                         "placeholder": "Enter Item Type"}),
        #     'no_items': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter No Items "}),
        #     'es_width': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter ES Width"}),
        #     'es_height': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                         "placeholder": "Enter Es Height "}),
        #     'fn_width': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter Final Width "}),
        #     'fn_height': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                         "placeholder": "Enter Final Height "}),
        #     'created_by': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                          "placeholder": "Enter Created BY "}),
        #     'updated_by': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                          "placeholder": "Enter Updated BY "}),
        #     'proposal_status': forms.ChoiceField(attrs={'class': 'form-control form-rounded',
        #
        #                                                 })
        # }

    def clean_proposal_id(self):
        proposal_id = self.cleaned_data['proposal_id']
        if len(proposal_id) < 4:
            raise forms.ValidationError("Id must be 4 numbers")
        return proposal_id

    labels = {
        'proposal_id': 'Proposal-ID',
        'proposal_status': 'Proposal Status',
        'proposal_amount': 'Proposal Amount',
        'item_type': 'Item Type',
        'no_items': 'No Items',
        'item_details': 'Item Details',
        'img': 'Image',
        'es_width': 'ES Width',
        'es_height': 'Es Height',
        'fn_width': 'Fn Width',
        'fn_height': 'Fn Height',
        'created_by': 'Created By',
        'created_date': 'Created Date',
        'updated_by': 'Update By',
        'updated_date': 'Updated By'

    }
