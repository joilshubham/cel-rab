from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import Item

import time


@shared_task
def worker_api(**params):
    time.sleep(20)
    item = params.get('item', '')
    id = params.get('id', '')

    item_data = get_object_or_404(Item, id=id)

    if item_data.item == item:
        item_data.status = 'completed'
    
    item_data.save()

    print(item_data)
    data = {
        "item":item_data.item,
        "id":item_data.id,
        "status":item_data.status,
    }
    print(data)
    return (data)

@shared_task
def tests(name, surname):
    full = name + ' ' + surname
    print(full)
    return full
    