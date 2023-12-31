from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.utils.dateparse import parse_datetime
from django.views import generic
from .forms import AddFormulaForm
from .models import Record, Formula, Adjuvant, Applicator, Park, Pesticide 

class IndexView(generic.ListView):
    template_name = "pesticides/index.html"
    context_object_name = "latest_records_list"

    def get_queryset(self):
        return Record.objects.order_by("date")[:5]

class DetailView(generic.DetailView):
    model = Record
    template_name = "pesticides/detail.html"

class FormulaView(generic.ListView):
    template_name = "pesticides/formula.html"
    context_object_name = "formulas"
    def get_queryset(self):
        return Formula.objects.all()

class FormulaDetailView(generic.DetailView):
    model = Formula
    template_name = "pesticides/formula_detail.html"

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
    
def update_record(request, record_id):
    formula_list = Formula.objects.all()
    applicators = Applicator.objects.all()
    parks = Park.objects.all()
    current_record = Record.objects.get(id=record_id)
    context = {'current_record': current_record,
               'formula_list': formula_list,
               'parks': parks,
               'applicators': applicators,
               }
    if request.method == "POST":
        new_record = current_record
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
        return redirect('pesticides:index')

    return render(request, 'pesticides/update_record.html', context)

def add_formula(request):
    
    form = AddFormulaForm(request.POST or None)
    if request.method == "POST":
        pesticide = Pesticide.objects.get(pk=request.POST['pesticide'])
        adjuvant = Adjuvant.objects.get(pk=request.POST['adjuvant'])
        new_formula = Formula()
        new_formula.name = request.POST['name']
        new_formula.pesticide_amount = request.POST['pesticide_amount']
        new_formula.adjuvant_amount = request.POST['adjuvant_amount']
        new_formula.pesticide = pesticide
        new_formula.adjuvant = adjuvant
        new_formula.save()
        messages.success(request, "Formula added")
        return redirect('pesticides:formula')
    return render(request, 'pesticides/add_formula.html', {'form':form})    