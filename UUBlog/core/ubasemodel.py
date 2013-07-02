#-*- coding:utf-8 -*-

from django.db import models


class UBaseModel(models.Model):
    class Meta:
        abstract =True

    def getModelResult(model,*orders,**wheres):

        ret=model.objects

        if wheres.items().count>0:
            ret=ret.filter(**wheres)

        for order in orders:
            ret=ret.order_by(order)

        return ret

    def Test(self):
        return self
    


