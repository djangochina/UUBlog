#-*- coding:utf-8 -*-
from django.db import models


class UBaseModel(models.Model):
  
    class Meta:
        abstract =True


    def Test(self):
        return self
    


