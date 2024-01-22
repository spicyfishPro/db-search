import json
import logging

from django.http import JsonResponse
from wxcloudrun.models import Counters
from django.db import connection
from django.shortcuts import render, HttpResponse
from .models import wheatinfo


logger = logging.getLogger('log')


def index(request):
    mother_name = request.GET.get('母本')
    father_name = request.GET.get('父本')

    if not mother_name or not father_name:
        return JsonResponse({'error': 'Missing parent parameter'}, status=400)

    # 使用Django ORM进行查询
    query_results = wheatinfo.objects.filter(mother=mother_name, father=father_name).values('id', 'title')

    # 将QuerySet转换为列表
    data_list = list(query_results)

    # 返回JSON响应
    return JsonResponse(data_list, safe=False)
