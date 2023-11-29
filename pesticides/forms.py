from django import forms
from .models import Record, Adjuvant, Formula, Park, Pesticide 


class AddFormulaForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label="")
    pesticide = forms.ChoiceField(widget=forms.Select, choices=[(p.id, p.name) for p in Pesticide.objects.all()]) 
    pesticide_amount = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Pesticide Amount:", "class":"form-control"}), label="")
    concentration = forms.ChoiceField(widget=forms.Select, choices=Formula.CONCENTRATION_CHOICES)
    adjuvant = forms.ChoiceField(widget=forms.Select, choices=[(a.id, a.name) for a in Adjuvant.objects.all()]) 
    adjuvant_amount = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Adjuvant Amount:", "class":"form-control"}), label="")
    adjuvant_concentration = forms.ChoiceField(widget=forms.Select, choices=Formula.CONCENTRATION_CHOICES)

    class Meta:
        model = Formula
        exclude = ['adjuvant']
        fields = ['name', 
                  'pesticide_amount', 
                  'pesticide',
                  'concentration',
                  'adjuvant_amount',
                  'adjuvant_concentration',
                  ]
