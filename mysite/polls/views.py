from django.http import HttpResponse, Http404
from django.shortcuts import render
from polls.models import DataSet
from django.views.decorators.csrf import csrf_exempt
import json
import csv
import os


def data_get(request):
    if request.method == 'GET':
        try:
            # p = Data.objects.get(first_field=first_field)
            data_query = DataSet.objects.all()

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
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    d = DataSet(date=row[0],
                                channel=row[1],
                                country=row[2],
                                os=row[3],
                                impressions=row[4],
                                clicks=row[5],
                                installs=row[6],
                                spend=row[7],
                                revenue=row[8])
                    d.save()
    return HttpResponse("Updated data")
