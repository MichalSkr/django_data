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
    """

    :param request:
    :return:
    """
    if request.method == 'GET':
        global data_query

        if not data_query:
            data_query = DataSet.objects.all()

        args = {'data': data_query}
        return render(request, 'detail.html', args)


@csrf_exempt
def data_get_specific(request):
    """

    :param request:
    :return:
    """
    global data_query
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            group_by = json_data.get('group_by', ["date"])  # default grouping will be by date
            order_by = json_data.get('sort_by', "")
            filter_by = json_data.get('filter_by', "")
            filters = {}
            for key in filter_by.keys():
                val = filter_by[key]
                if val:
                    if key == 'date_from':
                        key = 'date__gte'
                    if key == 'date_to':
                        key = 'date__lte'
                    filters[key] = val
            database_fields = [f.name for f in DataSet._meta.get_fields()]
            data_query = DataSet.objects.values(*group_by).filter(**filters).annotate(
                at_total_instance=F("installs"),
                CPI=Case(
                    When(at_total_instance=0, then=0),
                    default=F("spend") / F("installs"),
                    output_field=FloatField()
                )).annotate(s=Sum('clicks')).values(*database_fields)

            if order_by:
                args = []
                data_query = data_query.order_by(*args)

        except DataSet.DoesNotExist:
            raise Http404("Poll does not exist")
        args = {'data': data_query}
        return render(request, 'detail.html', args)


@csrf_exempt
def data_post(request):
    """

    :param request:
    :return:
    """
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
    """

    :param request:
    :return:
    """
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
