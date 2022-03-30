from django.urls import path

from .views import proposal_list, proposal_view, proposal_create, proposal_update, proposal_delete, \
    proposal_contract_create, pdf_generation_proposal

app_name = 'proposal'

urlpatterns = [

    path('proposal/list/', proposal_list, name='proposal_list'),
    path('proposal/view/<int:id>/', proposal_view, name='proposal_view'),
    path('proposal/create/', proposal_create, name='proposal_create'),
    path('proposal/update/<int:id>/', proposal_update, name='proposal_update'),
    path('proposal/delete/<int:id>/', proposal_delete, name='proposal_delete'),

    path('proposal/pdf/<int:id>', pdf_generation_proposal, name='proposal_pdf'),
    path('contract/proposal/<int:id>/', proposal_contract_create, name='proposal_contract_create'),


]
