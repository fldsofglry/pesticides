from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.utils.dateparse import parse_datetime
from .models import Record, Formula, Applicator, Park 

def index(request):
    latest_records_list = Record.objects.order_by("date")[:5]
    template = loader.get_template("pesticides/index.html")
    context = {"latest_records_list": latest_records_list}
    return HttpResponse(template.render(context, request))

def detail(request, record_id):
    pesticide_record = Record.objects.get(id=record_id)
    context = {'record': pesticide_record}
    return render(request, 'pesticides/detail.html', context)

def delete_record(request, record_id):
    delete_it = Record.objects.get(id=record_id)
    delete_it.delete()
    # messages.success(request, "Records Deleted Successfully")
    return redirect("pesticides:index")

def add_record(request):
    formula_list = Formula.objects.all()
    applicators = Applicator.objects.all()
    parks = Park.objects.all()


    template = loader.get_template("pesticides/add_record.html")
    context = {"formula_list": formula_list,
              "applicators": applicators,
                "parks": parks,
               }
    if request.method == "POST":
            print(request.POST)
            new_record = Record()
            applicator = Applicator.objects.get(pk=request.POST['applicator'])
            
            new_record.applicator = applicator
            
            park = Park.objects.get(pk=request.POST['park'])
            new_record.park = park
            formula = Formula.objects.get(pk=request.POST['formula'])
            new_record.formula = formula
            new_record.area_size = request.POST['area_size']
            new_record.targeted_species = request.POST['targeted_species']
            new_record.weather = request.POST['weather']
            new_record.date = parse_datetime(request.POST['date']+ " " + request.POST['time'])

            new_record.save()
            
            if new_record:
                # messages.success(request, "Record Added...")
                return redirect('pesticides:index')
                 
    else:
        return HttpResponse(template.render(context, request))