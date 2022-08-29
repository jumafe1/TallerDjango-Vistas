import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .logic import measurements_logic as mea
from django.core import serializers
from django.http import HttpResponse
@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = mea.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'aplication/json')
        else:
            measurements_dto = mea.get_measurements()
            measurements = serializers.serialize('json', measurements_dto)
            return HttpResponse(measurements, 'application/json')
    if request.method == 'POST':
        measurement_dto = mea.create_measurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')


@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurements = mea.get_measurements(pk)
        measurements_dto = serializers.serialize('json', measurements)
        return HttpResponse(measurements_dto, 'application/json')

    if request.method == 'PUT':
        measurement_dto = mea.update_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

    if request.method == 'DELETE':
        measurement_dto = mea.delete_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')






