from django import forms
from django.core import validators
from django.forms import modelformset_factory

from tasks.models import Task


class TaskForm(forms.ModelForm):
    task_id = forms.CharField(validators=[validators.MinLengthValidator(4)])

    class Meta:
        model = Task
        fields = ['task_id', 'sales_id', 'project_manager_id', 'project',
                  'task_name', 'task_status', 'item_type', 'no_items',
                  'end_date', 'img', 'task_delivery_date',
                  'item_details', 'fn_width', 'fn_height', 'created_by', 'created_date']
        # widgets = {
        #     'sales_id': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter Sales ID "}),
        #     'project_manager_id': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                                  "placeholder": "Enter Project Manager ID "}),
        #     'project': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                       "placeholder": "Enter Project "}),
        #     'task_name': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                         "placeholder": "Enter Task Name "}),
        #     'task_status': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                           "placeholder": "Enter Task Status "}),
        #     'item_type': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                         "placeholder": "Enter Item Type "}),
        #     'no_items': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter No Items "}),
        #     'end_date': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter End Date "}),
        #     'img': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                   "placeholder": "Enter Image "}),
        #     'task_delivery_date': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                                  "placeholder": "Enter Task Delivery Date "}),
        #     'fn_width': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                        "placeholder": "Enter Final Width "}),
        #     'fn_height': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                         "placeholder": "Enter Final Height "}),
        #     'project_plan_delivery_date': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                                          "placeholder": "Enter Project Plan Delivery Date "}),
        #     'contract_start_date': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                                   "placeholder": "Enter Contract Start Date"}),
        #     'project_delivery_date': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                                     "placeholder": "Enter Project Delivery Date"}),
        #     'contract_delivery_date': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                                      "placeholder": "Enter Contract Delivery Date"}),
        #     'item_details': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                            "placeholder": "Enter Item Details "}),
        #     'created_by': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #
        #                                          "placeholder": "Enter Created BY "}),
        #     'updated_by': forms.TextInput(attrs={'class': 'form-control form-rounded',
        #                                          "placeholder": "Enter Updated BY "}), }


TaskFormSet = modelformset_factory(
    Task, exclude=("sales_id", "project_manager_id", "project"), extra=1)
