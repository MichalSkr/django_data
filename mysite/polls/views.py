from django.http import HttpResponse, Http404
from django.shortcuts import render
from polls.models import DataSet
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, Count, Avg, Q, Case, F, FloatField, When
import json
import csv
import os

data_query = None


def data_get(request):
    if request.method == 'GET':
        global data_query

        if not data_query:
            data_query = DataSet.objects.all()

        args = {'data': data_query}
        return render(request, 'detail.html', args)


@csrf_exempt
def data_get_specific(request):
    global data_query
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            group_by = json_data['group_by'] if 'group_by' in json_data.keys() else ''
            order_by = json_data['sort_by'] if 'sort_by' in json_data.keys() else ''
            filter_by = json_data['filter_by'] if 'filter_by' in json_data.keys() else ''
            filters = {}
            for key in filter_by.keys():
                val = filter_by[key]
                if val:
                    if key == 'date_from':
                        key = 'date__gte'
                    if key == 'date_to':
                        key = 'date__lte'
                    filters[key] = val
            data_query = DataSet.objects.values('country', 'channel', 'date').filter(**filters).annotate(
                at_total_instance=F("installs"),
                CPI=Case(
                    When(at_total_instance=0, then=0),
                    default=F("spend") / F("installs"),
                    output_field=FloatField()
                ))
            if order_by:
                args = []
                data_query = data_query.order_by(*args)[:-1]

        except DataSet.DoesNotExist:
            raise Http404("Poll does not exist")
        args = {'data': data_query}
        return render(request, 'detail.html', args)


@csrf_exempt
def data_post(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        d = DataSet(date=json_data['date'],
                    channel=json_data['channel'],
                    country=json_data['country'],
                    os=json_data['os'],
                    impressions=json_data['impressions'],
                    clicks=json_data['clicks'],
                    installs=json_data['installs'],
                    spend=json_data['spend'],
                    revenue=json_data['revenue'])
        d.save()
        return HttpResponse("Got json data")


def upload_data_file(request):
    if request.method == 'GET':
        with open(os.path.join(os.getcwd(), r'polls\dataset.csv')) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            col_names = list()
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    col_names = row
                    line_count += 1
                else:
                    dict_values = {}
                    for i in range(len(row)):
                        dict_values[col_names[i]] = row[i]
                    d = DataSet(**dict_values)
                    d.save()
    return HttpResponse("Updated data")
