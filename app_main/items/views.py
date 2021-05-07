from __future__ import absolute_import
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from .models import Item
from .tasks import worker_api


class ProducerApi(APIView):
    def post(self, request, format = 'application/json'):
        item = request.data.get('item')
        item_inst = Item(item = item)
        item_inst.save()
        try:
            item_inst.save()
        except ValueError:
            return JsonResponse({'error':'payload needs to be in {{item:<value>}} format'})
        
        item_id = item_inst.id
        item_name = item_inst.item

        data = {
            "id": item_id,
            "item": item_name
        }

        worker_api.delay(item = item_name, id = item_id)

        return JsonResponse(data, status = status.HTTP_202_ACCEPTED)

        