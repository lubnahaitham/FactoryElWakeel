from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.template.loader import get_template
from xhtml2pdf import pisa
from clients.models import Client
from contracts.models import Contract
from projects.forms import ProjectForm
from projects.models import Project
from proposals.models import Proposal
from tasks.forms import TaskFormSet
from tasks.models import Task
from users.decorators import allowed_users


# Create your views here.

@login_required(login_url='user:login')
def project_list(request):
    context = {'project_list': Project.objects.all()}
    return render(request, "project/project_list.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['projectmanager', 'admin'])
def project_view(request, id):
    project_view = get_object_or_404(Project, pk=id)
    # c = project_view.contract
    # print(c)
    # p = c.proposal
    # cl = p.client

    task_view = Task.objects.filter(Q(project__id=project_view.id))

    client_view = get_object_or_404(Client, pk=id)
    context = {'project_view': project_view, 'task_view': task_view,
               'client_view': client_view}
    return render(request, "project/project_view.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['projectmanager', 'admin'])
def project_create(request, id=0):
    if 'project_id' in request.POST and 'project_name' in request.POST and 'item_type' in request.POST and \
            'no_items' in request.POST and 'item_details' in request.POST and \
            'img' in request.POST and 'fn_width' in request.POST and \
            'fn_height' in request.POST and\
            'created_date' in request.POST and 'updated_date' in request.POST and 'end_date' in request.POST and \
            'project_plan_delivery_date' in request.POST and 'project_delivery_date' in request.POST:

        project_id = request.POST['project_id']
        project_name = request.POST['project_name']
        item_type = request.POST['item_type']
        no_items = request.POST['no_items']
        item_details = request.POST['item_details']
        img = request.POST['img']
        fn_width = request.POST['fn_width']
        fn_height = request.POST['fn_height']
        created_date = request.POST['created_date']
        updated_date = request.POST['updated_date']
        end_date = request.POST['end_date']
        project_plan_delivery_date = request.POST['project_plan_delivery_date']
        project_delivery_date = request.POST['project_delivery_date']

    else:
        project_id = False
        project_name = False
        item_type = False
        no_items = False
        item_details = False
        img = False
        fn_width = False
        fn_height = False
        created_date = False
        updated_date = False
        end_date = False
        project_plan_delivery_date = False
        project_delivery_date = False

    if request.method == "GET":
        if id == 0:
            form = ProjectForm()
        else:
            project = get_object_or_404(Project, pk=id)
            form = ProjectForm(instance=project)
        return render(request, "project/project_create.html", {'form': form})
    else:
        if request.method == "POST":
            if id == 0:
                form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/project/list')


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['projectmanager', 'admin'])
def project_update(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/project/list')

    return render(request, 'project/project_update.html', {'form': form})


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['projectmanager', 'admin'])
def project_delete(request, id):
    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect('/project/list')


@login_required(login_url='user:login')
def pdf_generation_project(request, id):
    client_pdf = get_object_or_404(Client, pk=id)
    proposal_pdf = get_object_or_404(Proposal, pk=id)
    contract_pdf = get_object_or_404(Contract, pk=id)
    project_pdf = get_object_or_404(Project, pk=id)
    task_pdf = Task.objects.filter(Q(project__id=project_pdf.id))

    template_path = 'project/project_pdf.html'
    data = {
        "client_pdf": client_pdf, "proposal_pdf": proposal_pdf,
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['projectmanager', 'admin'])
def task_project_create(request, id):
    project_data = Project.objects.get(id=id)
    contract_to_join = project_data.contract
    proposal_to_join = contract_to_join.proposal
    client_to_join = contract_to_join.proposal.client
    initial = [{'project_data': project_data}]
    formset = TaskFormSet(queryset=Task.objects.none(), initial=initial)

    if request.method == 'POST':
        print(request.POST)
        formset = TaskFormSet(request.POST or None, request.FILES)
        if formset.is_valid():
            print(formset.is_valid())
            project = Project.objects.get(id=id)
            obj = formset.save(commit=False)
            for member in obj:
                member.project = project
                member.save()

            return redirect('/task/list')
    context = {'task_formset': formset, 'project_data': project_data, 'contract_to_join': contract_to_join,
               'proposal_to_join': proposal_to_join, 'client_to_join': client_to_join}
    return render(request, 'task/task_create.html', context)
