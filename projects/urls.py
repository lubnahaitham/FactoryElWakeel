from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import project_list, project_view, project_create, project_update, project_delete, task_project_create, \
    pdf_generation_project, task_list, task_view, task_create, task_update, task_delete, pdf_generation_task

app_name = 'project'

urlpatterns = [

    path('project/list/', project_list, name='project_list'),
    path('project/view/<int:id>/', project_view, name='project_view'),
    path('project/create/', project_create, name='project_create'),
    path('project/update/<int:id>/', project_update, name='project_update'),
    path('project/delete/<int:id>/', project_delete, name='project_delete'),

    path('project/pdf/<int:id>', pdf_generation_project, name='project_pdf'),
    path('project/task/<int:id>/', task_project_create, name='task_project_create'),

    path('task/list/', task_list, name='task_list'),
    path('task/view/<int:id>/', task_view, name='task_view'),
    path('task/create/', task_create, name='task_create'),
    path('task/update/<int:id>/', task_update, name='task_update'),
    path('task/delete/<int:id>/', task_delete, name='task_delete'),

    path('task/pdf/<int:id>', pdf_generation_task, name='task_pdf'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)