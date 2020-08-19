from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from ActivitiesApp.models import GroupActivityModel, ActivityPartModel, ActivityModel, GroupModel
from .forms import TaskForm
from .models import TaskModel, TaskPartsModel
from django.contrib.auth.decorators import login_required


@login_required
def task_list(request):
    # print(TaskModel.objects.filter(group__workCenter__contains='LC'))
    # print(TaskModel.objects.filter(taskpartsmodel__user__exact=request.user))
    return render(request, 'listTasks.html', {'header': 'Outstanding Tasks',
                                              'tasks': TaskModel.objects.all()})


@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():

            if TaskModel.objects.filter(taskName=form.cleaned_data['taskName']).count() > 0:
                messages.error(request, "Task already exists")
                return redirect('addtask')

            taskMy = form.save()
            groupname = form.cleaned_data['group']

            groupactivitylist = GroupActivityModel.objects.filter(group=groupname)

            for activity in groupactivitylist:
                required_list = ActivityPartModel.objects.filter(activity=activity.activity)
                for required in required_list:
                    temp = TaskPartsModel(task=taskMy,
                                          part=required.part,
                                          quantityRequired=required.quantity,
                                          quantityCompleted=0,
                                          )
                    temp.save()

            return redirect('tasks')
    else:
        form = TaskForm()
        return render(request, 'addTask.html', {'taskform': form})


@login_required
def info_task_activities(request, taskid):
    task = get_object_or_404(TaskModel, id=taskid)
    activities = GroupActivityModel.objects.filter(group=task.group)
    return render(request, 'infoTaskActivities.html', {'header': 'Grouped Activities',
                                                       'taskid': taskid,
                                                       'taskactivities': activities})


@login_required
def info_task_parts(request, taskid, activityid):
    if request.method == "POST":
        for completed in request.POST:
            try:
                updatedvalue = get_object_or_404(TaskPartsModel, id=int(completed))
                updatedvalue.updateQuantity(int(request.POST[completed]))
            except ValueError:
                pass
    reqParts = ActivityPartModel.objects.filter(activity=activityid)
    parts = TaskPartsModel.objects \
        .filter(task=taskid) \
        .filter(part_id__in=reqParts.values_list("id"))
    print(TaskPartsModel.objects.filter(task=taskid))
    print(parts)
    if get_object_or_404(TaskModel, id=taskid).group.workCenter.wcType == 'PK':
        return render(request, 'infoTaskParts.html', {'header': 'Kits',
                                                      'parts': parts})
