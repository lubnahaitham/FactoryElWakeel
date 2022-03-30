from django.urls import path

from .views import document_list, document_view, document_create, document_update, document_delete,\
    pdf_generation, document_task_create
app_name = 'document'


urlpatterns = [

    path('document/list/', document_list, name='document_list'),
    path('document/view/<int:id>/', document_view, name='document_view'),
    path('document/create/', document_create, name='document_create'),
    path('document/update/<int:id>/', document_update, name='document_update'),
    path('document/delete/<int:id>/', document_delete, name='document_delete'),

    path('document/pdf/<int:id>', pdf_generation, name='document_pdf'),
    path('task/document/<int:id>/', document_task_create, name='document_task_create'),

]
