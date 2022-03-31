from django import forms
from django.core import validators

from clients.models import Client
from django.utils.translation import gettext_lazy as _


class ClientForm(forms.ModelForm):
    # client_name = forms.CharField(label=_(u'Client Name'),
    #                               widget=forms.TextInput(attrs={'class': 'form-control form-rounded',
    #                                                             "placeholder": "Enter Client Name"}))
    # client_personal_id = forms.CharField(label=_(u'Client Personal-ID'))
    # client_home_tel = forms.CharField(label=_('Client Home Telephone'))

    client_personal_id = forms.CharField(validators=[validators.MinLengthValidator(4)],
                                         widget=forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                                       "placeholder": "Enter Client Personal ID"}))

    class Meta:
        model = Client
        fields = ['client_name', 'client_personal_id', 'client_home_tel', 'client_office_tel', 'client_mobile',
                  'client_address', 'client_province', 'client_nghood', 'client_pobox',
                  'contact_name', 'contact_id', 'contact_mobile',
                  'created_by', 'created_date',
                  'updated_by', 'updated_date']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                  }),
            'client_home_tel': forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                      }),
            'client_office_tel': forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                        }),
            'client_mobile': forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                    }),
            'client_address': forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                     }),
            'client_province': forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                      }),
            'client_nghood': forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                    }),
            'client_pobox': forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                   }),
            'contact_name': forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                   }),
            'contact_id': forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                 }),
            'contact_mobile': forms.TextInput(attrs={'class': 'form-control form-rounded',
                                                     }),
            'created_by': forms.Select(attrs={'class': 'regDropDown form-rounded form-rounded',
                                              }),
            'created_date': forms.Select(attrs={'class': 'regDropDown form-rounded',
                                                }),
            'updated_by': forms.Select(attrs={'class': 'regDropDown form-rounded form-rounded',
                                              }),

        }

    def clean_personal_id(self):
        client_personal_id = self.cleaned_data['client_personal_id']
        contact_id = self.cleaned_data['contact_id']

        if len(client_personal_id) < 4 and len(contact_id) < 4:
            raise forms.ValidationError("Id must be 8 numbers")
        return client_personal_id, contact_id

    # labels = {
    #     'client_name': 'Client Name',
    #     'client_personal_id': 'ClientPersonal-ID',
    #     'client_home_tel': 'ClientHome-Tel',
    #     'client_office_tel': 'ClientOffice-Tel',
    #     'client_mobile': 'Client Mobile',
    #     'client_address': 'Client Address',
    #     'client_province': 'Client Province',
    #     'client_nghood': 'Client NGhood',
    #     'client_pobox': 'Client PoBox',
    #     'contact_name': 'Contact Name',
    #     'contact_id': 'Contact-PID',
    #     'contact_mobile': 'Contact Mobile',
    #     'created_by': 'Created By',
    #     'created_date': 'Created Date',
    #     'updated_by': 'Update By',
    #     'updated_date': 'Updated By'
    #
    # }
