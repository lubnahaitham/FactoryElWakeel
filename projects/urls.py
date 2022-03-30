from django.urls import path

from .views import project_list, project_view, project_create, project_update, project_delete, task_project_create,\
    pdf_generation_project
app_name = 'project'

urlpatterns = [

    path('project/list/', project_list, name='project_list'),
    path('project/view/<int:id>/', project_view, name='project_view'),
    path('project/create/', project_create, name='project_create'),
    path('project/update/<int:id>/', project_update, name='project_update'),
    path('project/delete/<int:id>/', project_delete, name='project_delete'),

    path('project/pdf/<int:id>', pdf_generation_project, name='project_pdf'),
    path('project/task/<int:id>/', task_project_create, name='task_project_create'),


]
