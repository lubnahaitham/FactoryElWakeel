from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import contract_list, contract_view, contract_create, contract_update, contract_delete, \
    pdf_generation_contract, contract_project_create
app_name = 'contract'

urlpatterns = [
 

    path('contract/list/', contract_list, name='contract_list'),
    path('contract/view/<int:id>/', contract_view, name='contract_view'),
    path('contract/create/', contract_create, name='contract_create'),
    path('contract/update/<int:id>/', contract_update, name='contract_update'),
    path('contract/delete/<int:id>/', contract_delete, name='contract_delete'),

    path('contract/pdf/<int:id>', pdf_generation_contract, name='contract_pdf'),
    path('project/contract/<int:id>/', contract_project_create, name='contract_project_create'),
   

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)