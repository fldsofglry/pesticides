from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Record

def index(request):
    latest_records_list = Record.objects.order_by("date")[:5]
    template = loader.get_template("pesticides/index.html")
    context = {"latest_records_list": latest_records_list}
    return HttpResponse(template.render(context, request))

def detail(request, record_id):
    pesticide_record = Record.objects.get(id=record_id)
    context = {'record': pesticide_record}
    return render(request, 'pesticides/detail.html', context)
