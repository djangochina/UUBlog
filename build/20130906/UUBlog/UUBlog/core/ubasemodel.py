#-*- coding:utf-8 -*-

from django.db import models


class UBaseModel(models.Model):
  
    class Meta:
        abstract =True

    def getModelResult(model,count=None,*orders,**wheres):

        ret=model.objects.filter(**wheres)

        for order in orders:
            ret=ret.order_by(order)
        if count:
            return ret[:count]
        return ret

    def Test(self):
        return self
    


