# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
from TestModel.models import customers
 
# 数据库操作
def testdb(request):
    # 初始化
    # 输出所有数据
    response1=''
    list = customers.objects.all()
    for var in list:
        response1 += str(var.id) + var.loginname
    response = response1
    return HttpResponse("<p>" + response + "</p>")