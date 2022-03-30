from clients.models import Client
from contracts.forms import ContractForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from users.decorators import allowed_users
from xhtml2pdf import pisa

from .forms import ProposalForm
from .models import Proposal


# Create your views here.

@login_required(login_url='user:login')
def proposal_list(request):
    context = {'proposal_list': Proposal.objects.all()}
    return render(request, "proposal/proposal_list.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def proposal_view(request, id):
    client_views = Client.objects.get(pk=id)
    proposal_view = get_object_or_404(Proposal, pk=id)
    context = {'proposal_view': proposal_view, 'client_views': client_views}
    return render(request, "proposal/proposal_view.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def proposal_create(request, id=0):
    if 'proposal_id' in request.POST and 'item_type' in request.POST and \
            'no_items' in request.POST and 'item_details' in request.POST and \
            'img' in request.POST and 'es_width' in request.POST and \
            'es_height' in request.POST and 'fn_width' in request.POST and \
            'fn_height' in request.POST and \
            'created_date' in request.POST and 'updated_date' in request.POST:

        proposal_id = request.POST['proposal_id']
        item_type = request.POST['item_type']
        no_items = request.POST['no_items']
        item_details = request.POST['item_details']
        img = request.POST['img']
        es_width = request.POST['es_width']
        es_height = request.POST['es_height']
        fn_width = request.POST['fn_width']
        fn_height = request.POST['fn_height']
        created_date = request.POST['created_date']
        updated_date = request.POST['updated_date']

    else:
        proposal_id = False
        item_type = False
        no_items = False
        item_details = False
        img = False
        es_width = False
        es_height = False
        fn_width = False
        fn_height = False
        created_date = False
        updated_date = False

    if request.method == "GET":
        if id == 0:
            form = ProposalForm()
        else:
            proposal = get_object_or_404(Proposal, pk=id)
            form = ProposalForm(instance=proposal)
        return render(request, "proposal/proposal_create.html", {'form': form})
    else:
        if request.method == "POST":
            if id == 0:
                form = ProposalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/proposal/list')


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def proposal_update(request, id):
    proposal = get_object_or_404(Proposal, pk=id)
    form = ProposalForm(instance=proposal)

    if request.method == 'POST':
        form = ProposalForm(request.POST, request.FILES, instance=proposal)
        if form.is_valid():
            form.save()
            return redirect('/proposal/list')

    return render(request, 'proposal/proposal_update.html', {'form': form})


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def proposal_delete(request, id):
    proposal = get_object_or_404(Proposal, pk=id)
    proposal.delete()
    return redirect('/proposal/list')


@login_required(login_url='user:login')
def pdf_generation_proposal(request, id):
    client_pdf = get_object_or_404(Client, pk=id)
    proposal_pdf = get_object_or_404(Proposal, pk=id)

    template_path = 'proposal/proposal_pdf.html'
    data = {
        "client_pdf": client_pdf, "proposal_pdf": proposal_pdf,

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
@allowed_users(allowed_roles=['sales', 'admin'])
def proposal_contract_create(request, id):
    contract_data = Proposal.objects.get(id=id)
    client_to_join = contract_data.client
    form = ContractForm(instance=contract_data)

    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, initial={'contract_data': contract_data})
        if form.is_valid():
            proposal = Proposal.objects.get(pk=id)
            obj = form.save(commit=False)
            obj.proposal = proposal
            obj.save()

        return redirect('/contract/list')
    context = {'form': form, 'contract_data': contract_data, 'client': client_to_join}
    return render(request, 'contract/contract_create.html', context)
