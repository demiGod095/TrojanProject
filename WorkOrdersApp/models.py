from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db import models
from simple_history.models import HistoricalRecords
from PartsApp.models import *


# Create your models here.
from ActivitiesApp.models import GroupModel, ActivityModel
from PartsApp.models import PartModel


class TaskModel(models.Model):
    taskName = models.CharField(max_length=50)
    fleetNumber = models.CharField(max_length=50)
    group = models.ForeignKey(GroupModel, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.taskName) + " - " + str(self.group)


class TaskPartsModel(models.Model):
    task = models.ForeignKey(TaskModel, on_delete=models.PROTECT)
    part = models.ForeignKey(PartModel, on_delete=models.PROTECT)
    quantityRequired = models.IntegerField()
    quantityCompleted = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    history = HistoricalRecords()

    def updateQuantity(self, newval):
        change = newval-self.quantityCompleted
        self.part.stockOnHand -= change
        self.quantityCompleted = newval
        self.save()
        self.part.save()

    def __str__(self):
        return str(self.part)
