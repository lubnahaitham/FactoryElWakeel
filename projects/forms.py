from django import forms
from django.core import validators

from projects.models import Project


class ProjectForm(forms.ModelForm):
    project_id = forms.CharField(validators=[validators.MinLengthValidator(4)])

    class Meta:
        model = Project
        fields = ['project_id', 'project_status',
                  'project_name', 'sales', 'project_manager',
                  'item_type', 'no_items',
                  'item_details', 'fn_width', 'fn_height', 'img',
                  'end_date', 'project_plan_delivery_date', 'project_delivery_date',
                  'contract_start_date', 'contract_delivery_date', 'created_by', 'updated_by', 'created_date',
                  'updated_date']
        # widgets = {
        #     'project_status': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                              "placeholder": "Enter Project Status "}),
        #     'project_name': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                            "placeholder": "Enter Project Name "}),
        #     'sales': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                     "placeholder": "Enter Sales "}),
        #     'project_manager': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                               "placeholder": "Enter Project Manager "}),
        #     'item_type': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                         "placeholder": "Enter Item Type "}),
        #     'no_items': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter No Items "}),
        #     'item_details': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                            "placeholder": "Enter Item Details "}),
        #     'fn_width': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter Final Width "}),
        #     'fn_height': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                         "placeholder": "Enter Final Height "}),
        #     'img': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                   "placeholder": "Enter Image "}),
        #     'end_date': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter End Date "}),
        #     'project_plan_delivery_date': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                                          "placeholder": "Enter Project Plan Delivery Date "}),
        #     'contract_start_date': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                                   "placeholder": "Enter Contract Start Date"}),
        #     'project_delivery_date': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                                     "placeholder": "Enter Project Delivery Date"}),
        #     'contract_delivery_date': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                                      "placeholder": "Enter Contract Delivery Date"}),
        #     'created_by': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                          "placeholder": "Enter Created BY "}),
        #     'updated_by': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                          "placeholder": "Enter Updated BY "}), }

    def clean_project_id(self):
        project_id = self.cleaned_data['project_id']
        if len(project_id) < 4:
            raise forms.ValidationError("Id must be 4 numbers")
        return project_id

    labels = {
        'project_id': 'Project ID',
        'project_status': 'Project Status',
        'project_name': 'Project Name',
        'sales': 'Sales-ID',
        'project_manager': 'Project Manager-ID',
        'item_type': 'Item Type',
        'no_items': 'No Items',
        'item_details': 'Item Details',
        'fn_width': 'Width',
        'fn_height': 'Height',
        'end_date': 'End Date',
        'project_plan_delivery_date': 'Project Plan Delivery Date',
        'project_delivery_date': 'Project Delivery Date',
        'created_by': 'Created By',
        'created_date': 'Created Date',
        'updated_by': 'Update By',
        'updated_date': 'Updated By'
        # 'item_type': 'Item Type',
        # 'no_items': 'No Items',
        # 'item_details': 'Item Details',
        # 'fn_width': 'Width',
        # 'fn_height': 'Height',
        # 'img': 'Image',

    }