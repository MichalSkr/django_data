from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from polls.models import DataSet
from django.views.decorators.csrf import csrf_exempt
import json


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