from django import forms
from django.core import validators
from contracts.models import Contract



class ContractForm(forms.ModelForm):
    contract_id = forms.CharField(validators=[validators.MinLengthValidator(4)])

    class Meta:
        model = Contract
        fields = ['contract_id', 'contract_status',
                  'item_type', 'no_items',
                  'item_details', 'fn_width', 'fn_height',
                  'img', 'contract_start_date', 'contract_delivery_date',
                  'created_by', 'created_date', 'updated_by', 'updated_date']
        # widgets = {
        #     'contract_status': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                               "placeholder": "Enter Contract Status "}),
        #     'item_type': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                         "placeholder": "Enter Item Type "}),
        #     'no_items': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter No Item "}),
        #     'item_details': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                            "placeholder": "Enter Item Details "}),
        #     'fn_width': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter Final Width "}),
        #     'fn_height': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                         "placeholder": "Enter Final Height "}),
        #     'img': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                   "placeholder": "Enter Image "}),
        #     'created_by': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                          "placeholder": "Enter Created BY "}),
        #     'updated_by': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                          "placeholder": "Enter Updated BY "}), }

    def clean_contract_id(self):
        contract_id = self.cleaned_data['contract_id']
        if len(contract_id) < 4:
            raise forms.ValidationError("Id must be 4 numbers")
        return contract_id

    labels = {
        'contract_id': 'Contract ID',
        'contract_status': 'Contract Status',
        'item_type': 'Item Type',
        'no_items': 'No Items',
        'item_details': 'Item Details',
        'fn_width': 'Width',
        'fn_height': 'Height',
        'img': 'Image',
        'contract_start_date': 'Contract Start Date',
        'contract_delivery_date': 'Contract Delivery Date',
        'created_by': 'Created By',
        'created_date': 'Created Date',
        'updated_by': 'Update By',
        'updated_date': 'Updated By'
    }

