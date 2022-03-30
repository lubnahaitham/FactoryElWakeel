from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from clients.models import Client
from contracts.forms import ContractForm
from contracts.models import Contract
from projects.forms import ProjectForm
from proposals.models import Proposal
from users.decorators import allowed_users
from xhtml2pdf import pisa
from django.template.loader import get_template


# Create your views here.

@login_required(login_url='user:login')
def contract_list(request):
    context = {'contract_list': Contract.objects.all()}
    return render(request, "contract/contract_list.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def contract_view(request, id):
    context = {'contract_view': get_object_or_404(Contract, pk=id)}
    return render(request, "contract/contract_view.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def contract_create(request, id=0):
    if 'contract_id' in request.POST and 'item_type' in request.POST and \
            'no_items' in request.POST and 'item_details' in request.POST and \
            'img' in request.POST and 'es_width' in request.POST and \
            'es_height' in request.POST and 'fn_width' in request.POST and \
            'fn_height' in request.POST and 'contract_start_date' in request.POST and \
            'contract_delivery_date' in request.POST and 'created_date' in request.POST and 'updated_date' in request.POST:

        contract_id = request.POST['contract_id']
        item_type = request.POST['item_type']
        no_items = request.POST['no_items']
        item_details = request.POST['item_details']
        img = request.POST['img']
        es_width = request.POST['es_width']
        es_height = request.POST['es_height']
        fn_width = request.POST['fn_width']
        fn_height = request.POST['fn_height']
        contract_start_date = request.POST['contract_start_date']
        contract_delivery_date = request.POST['contract_delivery_date']
        created_date = request.POST['created_date']
        updated_date = request.POST['updated_date']

    else:
        contract_id = False
        item_type = False
        no_items = False
        item_details = False
        img = False
        es_width = False
        es_height = False
        fn_width = False
        fn_height = False
        contract_start_date = False
        contract_delivery_date = False
        created_date = False
        updated_date = False

    if request.method == "GET":
        if id == 0:
            form = ContractForm()
        else:
            contract = get_object_or_404(Contract, pk=id)
            form = ContractForm(instance=contract)
        return render(request, "contract/contract_create.html", {'form': form})
    else:
        if request.method == "POST":
            if id == 0:
                form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/contract/list')


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def contract_update(request, id):
    contract = get_object_or_404(Contract, pk=id)
    form = ContractForm(instance=contract)

    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('/contract/list')

    return render(request, 'contract/contract_update.html', {'form': form})


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def contract_delete(request, id):
    contract = get_object_or_404(Contract, pk=id)
    contract.delete()
    return redirect('/contract/list')


@login_required(login_url='user:login')
def pdf_generation_contract(request, id):
    client_pdf = get_object_or_404(Client, pk=id)
    proposal_pdf = get_object_or_404(Proposal, pk=id)
    contract_pdf = get_object_or_404(Contract, pk=id)

    template_path = 'contract/contract_pdf.html'
    data = {
        "client_pdf": client_pdf, "proposal_pdf": proposal_pdf,
        "contract_pdf": contract_pdf

    }
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="report.pdf"'

    template = get_template(template_path)

    html = template.render(data)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding='UTF-8')
    # if error then show some fun view
    if pisa_status.err:
        return HttpResponse(html)
    return response


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'projectmanager', 'admin'])
def contract_project_create(request, id):
    contract_project_data = Contract.objects.get(id=id)
    proposal_to_join = contract_project_data.proposal
    client_to_join = contract_project_data.proposal.client
    form = ProjectForm(instance=contract_project_data)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,
                           initial={'contract_project_data': contract_project_data})
        if form.is_valid():
            contract = Contract.objects.get(pk=id)
            obj = form.save(commit=False)
            obj.contract = contract
            obj.save()

            return redirect('/project/list')
    context = {'form': form, 'contract_project_data': contract_project_data, 'proposal_to_join': proposal_to_join,
               'client_to_join': client_to_join}
    return render(request, 'project/project_create.html', context)
