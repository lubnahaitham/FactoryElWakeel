from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from clients.models import Client
from contracts.models import Contract
from documents.forms import DocumentForm
from documents.models import Document
from projects.models import Project
from proposals.models import Proposal
from tasks.models import Task
from users.decorators import allowed_users
from xhtml2pdf import pisa
from django.template.loader import get_template

# Create your views here.

@login_required(login_url='user:login')
def document_list(request):
    context = {'document_list': Document.objects.all()}
    return render(request, "document/document_list.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def document_view(request, id):
    document_data_view = get_object_or_404(Document, pk=id)
    client_data_view = get_object_or_404(Client, pk=id)
    proposal_data_view = get_object_or_404(Proposal, pk=id)
    contract_data_view = get_object_or_404(Contract, pk=id)
    project_data_view = get_object_or_404(Project, pk=id)
    task_data_view = get_object_or_404(Task, pk=id)
    context = {'document_data_view': document_data_view, 'client_data_view': client_data_view,
               'proposal_data_view': proposal_data_view, 'contract_data_view': contract_data_view,
               'project_data_view': project_data_view, 'task_data_view': task_data_view
               }
    return render(request, "document/document_view.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def document_create(request, id=0):
    if 'document_id' in request.POST and 'document_name' in request.POST and 'document_type' in request.POST and \
            'created_date' in request.POST and 'updated_date' in request.POST:

        document_id = request.POST['document_id']
        document_name = request.POST['document_name']
        document_type = request.POST['document_type']
        created_date = request.POST['created_date']
        updated_date = request.POST['updated_date']


    else:
        document_id = False
        document_name = False
        document_type = False
        created_date = False
        updated_date = False

    if request.method == "GET":
        if id == 0:
            form = DocumentForm()
        else:
            document = get_object_or_404(Document, pk=id)
            form = DocumentForm(instance=document)
        return render(request, "document/document_create.html", {'form': form})
    else:
        if request.method == "POST":
            if id == 0:
                form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/document/list')


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def document_update(request, id):
    document = get_object_or_404(Document, pk=id)
    form = DocumentForm(instance=document)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('/document/list')

    return render(request, 'document/document_update.html', {'form': form})


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['sales', 'admin'])
def document_delete(request, id):
    document = get_object_or_404(Document, pk=id)
    document.delete()
    return redirect('/document/list')

@login_required(login_url='user:login')
def pdf_generation(request, id):
    document_pdf = get_object_or_404(Document, pk=id)
    client_pdf = get_object_or_404(Client, pk=id)
    proposal_pdf = get_object_or_404(Proposal, pk=id)
    contract_pdf = get_object_or_404(Contract, pk=id)
    project_pdf = get_object_or_404(Project, pk=id)
    task_pdf = get_object_or_404(Task, pk=id)
    template_path = 'document/document_pdf.html'
    data = {
        "document_pdf": document_pdf, "client_pdf": client_pdf, "proposal_pdf": proposal_pdf,
        "contract_pdf": contract_pdf, "project_pdf": project_pdf, "task_pdf": task_pdf
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


def document_task_create(request, id):
    task_data = Task.objects.get(id=id)
    project_to_join = task_data.project
    contract_to_join = project_to_join.contract
    proposal_to_join = contract_to_join.proposal
    client_to_join = proposal_to_join.client
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,
                            initial={'task_data': task_data})
        if form.is_valid():
            task = Task.objects.get(pk=id)
            obj = form.save(commit=False)
            obj.task = task
            obj.save()

            return redirect('/document/list')
    context = {'form': form, 'task_data': task_data, 'project_to_join': project_to_join,
               'contract_to_join': contract_to_join, 'proposal_to_join': proposal_to_join,
               'client_to_join': client_to_join}
    return render(request, 'document/document_create.html', context)
