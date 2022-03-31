from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import client_list, client_view, client_create, client_update, \
    client_delete, proposal_client_create, pdf_generation_client

app_name = 'client'

urlpatterns = [

    path('client/list/', client_list, name='client_list'),
    path('client/view/<int:id>/', client_view, name='client_view'),
    path('client/create/', client_create, name='client_create'),
    path('client/update/<int:id>/', client_update, name='client_update'),
    path('client/delete/<int:id>/', client_delete, name='client_delete'),

    path('client/pdf/<int:id>', pdf_generation_client, name='client_pdf'),

    path('client/proposal/<int:id>/', proposal_client_create, name='proposal_client_create'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
