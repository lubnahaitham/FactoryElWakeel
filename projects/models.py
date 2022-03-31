from django.contrib.auth.models import User
from django.db import models

from contracts.models import Contract


# Create your models here.

class Project(models.Model):
    PROJECT_STATUS = (
        ('A', 'A'),
        ('B', 'B'),
    )

    project_id = models.CharField(max_length=255, null=True, blank=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='contract_project', null=True,
                                 blank=True)
    project_name = models.CharField(max_length=255, null=True, blank=True)
    project_status = models.CharField(
        max_length=255, choices=PROJECT_STATUS, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    project_plan_delivery_date = models.DateField(null=True, blank=True)
    project_delivery_date = models.DateField(null=True, blank=True)
    contract_start_date = models.DateField(null=True, blank=True)
    contract_delivery_date = models.DateField(null=True, blank=True)
    sales = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='employee_sales')
    project_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                        related_name='pj_manager_employee')
    item_type = models.CharField(max_length=255, null=True, blank=True)
    no_items = models.CharField(max_length=255, null=True, blank=True)
    item_details = models.CharField(max_length=255, null=True, blank=True)
    fn_width = models.FloatField(null=True, blank=True)
    fn_height = models.FloatField(null=True, blank=True)
    img = models.ImageField(upload_to="images/", null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='create_project', null=True,
                                   blank=True)
    created_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='update_project', null=True,
                                   blank=True)
    updated_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    TASK_STATUS = (
        ('A', 'A'),
        ('B', 'B'),
    )

    task_id = models.CharField(max_length=255, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name='task_project')

    sales_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='task_sales_employee')
    project_manager_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                           related_name='task_pj_manager_employee')
    task_name = models.CharField(max_length=255, null=True, blank=True)
    item_type = models.CharField(max_length=255, null=True, blank=True)
    no_items = models.CharField(max_length=255, null=True, blank=True)
    item_details = models.CharField(max_length=255, null=True, blank=True)
    fn_width = models.FloatField(null=True, blank=True)
    fn_height = models.FloatField(null=True, blank=True)
    task_delivery_date = models.DateField(null=True, blank=True)
    task_status = models.CharField(max_length=255, choices=TASK_STATUS, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    img = models.ImageField(upload_to="images/", null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='create_task', null=True,
                                   blank=True)
    created_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.task_id