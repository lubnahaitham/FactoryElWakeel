from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import task_list, task_view, task_update, task_delete,\
    task_create, pdf_generation_task

app_name = 'task'

urlpatterns = [

    path('task/list/', task_list, name='task_list'),
    path('task/view/<int:id>/', task_view, name='task_view'),
    path('task/create/', task_create, name='task_create'),
    path('task/update/<int:id>/', task_update, name='task_update'),
    path('task/delete/<int:id>/', task_delete, name='task_delete'),

    path('task/pdf/<int:id>', pdf_generation_task, name='task_pdf'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)