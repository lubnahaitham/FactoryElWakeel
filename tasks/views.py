from clients.models import Client
from contracts.models import Contract
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from projects.models import Project
from tasks.forms import TaskForm, TaskFormSet
from tasks.models import Task
from users.decorators import allowed_users
from xhtml2pdf import pisa


# Create your views here.

@login_required(login_url='user:login')
def task_list(request):
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, "task/task_list.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['projectmanager', 'admin'])
def task_view(request, id):
    context = {'task_view': get_object_or_404(Task, pk=id)}
    return render(request, "task/task_view.html", context)


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['projectmanager', 'admin'])
def task_create(request, id=0):
    if 'task_id' in request.POST and 'task_name' in request.POST and 'item_type' in request.POST and \
            'no_items' in request.POST and 'item_details' in request.POST and \
            'img' in request.POST and 'fn_width' in request.POST and \
            'fn_height' in request.POST and 'task_delivery_date' in request.POST and \
            'end_date' in request.POST and 'created_date' in request.POST:

        task_id = request.POST['task_id']
        task_name = request.POST['task_name']
        item_type = request.POST['item_type']
        no_items = request.POST['no_items']
        item_details = request.POST['item_details']
        img = request.POST['img']
        fn_width = request.POST['fn_width']
        fn_height = request.POST['fn_height']
        task_delivery_date = request.POST['task_delivery_date']
        end_date = request.POST['end_date']
        created_date = request.POST['created_date']


    else:
        task_id = False
        task_name = False
        item_type = False
        no_items = False
        item_details = False
        img = False
        fn_width = False
        fn_height = False
        task_delivery_date = False
        end_date = False
        created_date = False

    if request.method == "GET":
        if id == 0:
            # TaskFormset = formset_factory(TaskForm,max_num=10,extra=1)
            formset = TaskFormSet(queryset=Task.objects.none())
        else:
            task = get_object_or_404(Task, pk=id)
            formset = TaskFormSet(queryset=Task.objects.none())
        return render(request, "task/task_create.html", {'task_formset': formset})
    else:
        if request.method == "POST":
            if id == 0:
                formset = TaskFormSet(request.POST, request.FILES)

        if formset.is_valid():
            formset.save()

        return redirect('/task/list')


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['projectmanager', 'admin'])
def task_update(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/task/list')

    return render(request, 'task/task_update.html', {'form': form})


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['projectmanager', 'admin'])
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('/task/list')


@login_required(login_url='user:login')
def pdf_generation_task(request, id):
    client_pdf = get_object_or_404(Client, pk=id)
    project_pdf = get_object_or_404(Project, pk=id)
    contract_pdf = get_object_or_404(Contract, pk=id)
    task_pdf = get_object_or_404(Task, pk=id)

    template_path = 'task/task_pdf.html'
    data = {
        "client_pdf": client_pdf, "project_pdf": project_pdf,
        "contract_pdf": contract_pdf, "task_pdf": task_pdf,

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
