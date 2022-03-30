from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from clients.forms import ClientForm
from clients.models import Client
from proposals.forms import ProposalForm
from proposals.models import Proposal
from users.decorators import allowed_users
from xhtml2pdf import pisa


# Create your views here.

@login_required(login_url='user:login')
def client_list(request):
    context = {'client_list': Client.objects.all()}
    return render(request, "clients/client_list.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def client_view(request, id):
    proposal_views = Proposal.objects.get(pk=id)
    context = {'client_view': get_object_or_404(Client, pk=id), 'proposal_views': proposal_views}
    return render(request, "clients/client_view.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def client_create(request, id=0):
    if 'client_name' in request.POST and 'client_personal_id' in request.POST and 'client_home_tel' in request.POST and \
            'client_office_tel' in request.POST and 'client_mobile' in request.POST and 'client_address' in request.POST and \
            'client_province' in request.POST and 'client_nghood' in request.POST and 'client_pobox' in request.POST and \
            'contact_name' in request.POST and 'contact_id' in request.POST and 'contact_mobile' in request.POST and \
            'updated_date' in request.POST and 'created_date' in request.POST:

        client_name = request.POST['client_name']
        client_personal_id = request.POST['client_personal_id']
        client_home_tel = request.POST['client_home_tel']
        client_office_tel = request.POST['client_office_tel']
        client_mobile = request.POST['client_mobile']
        client_address = request.POST['client_address']
        client_province = request.POST['client_province']
        client_nghood = request.POST['client_nghood']
        client_pobox = request.POST['client_pobox']
        contact_name = request.POST['contact_name']
        contact_id = request.POST['contact_id']
        contact_mobile = request.POST['contact_mobile']
        created_date = request.POST['created_date']
        updated_date = request.POST['updated_date']

    else:
        client_name = False
        client_personal_id = False
        client_home_tel = False
        client_office_tel = False
        client_mobile = False
        client_address = False
        client_province = False
        client_nghood = False
        client_pobox = False
        contact_name = False
        contact_id = False
        contact_mobile = False
        created_date = False
        updated_date = False

    if request.method == "GET":
        if id == 0:
            form = ClientForm()
        else:
            client = get_object_or_404(Client, pk=id)
            form = ClientForm(instance=client)
        return render(request, "clients/client_create.html", {'form': form})
    else:
        if request.method == "POST":
            if id == 0:
                form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/client/list')


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def client_update(request, id):
    client = get_object_or_404(Client, pk=id)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()

            return redirect('/client/list')

    return render(request, 'clients/client_update.html', {'form': form})


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def client_delete(request, id):
    client = get_object_or_404(Client, pk=id)
    client.delete()
    return redirect('/client/list')


def pdf_generation_client(request, id):
    client_pdf = get_object_or_404(Client, pk=id)
    proposal_pdf = get_object_or_404(Proposal, pk=id)

    template_path = 'clients/client_pdf.html'
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
def proposal_client_create(request, id):
    client = Client.objects.get(pk=id)
    form = ProposalForm(instance=client)
    if request.method == 'POST':
        form = ProposalForm(request.POST, request.FILES,
                            initial={'client': client})
        if form.is_valid():
            client = Client.objects.get(pk=id)
            obj = form.save(commit=False)
            obj.client = client
            obj.save()
            return redirect('/proposal/list')
    context = {'form': form, 'client': client}
    return render(request, 'proposal/proposal_create.html', context)
