import json

from django.shortcuts import render
from django.shortcuts import render

from .forms import FDForm

# Create your views here.
def index(request):
	return render(request, 'index.html')

# Create your views here.
def fd(request):
	dataDictionary = {'amount':1000, 'intrest': 500}

	dataJSON  = json.dumps(dataDictionary)
	return render(request, 'fd_calculator.html', {'data': dataJSON })

def fd_calc(request):
	draw = None
	total_earning = None
	if request.method == "POST":
		form = FDForm(request.POST)
		if form.is_valid():
			amount = int(form.data.get('amount'))
			invested_amount = amount
			rate_of_intrest = float(form.data.get('rate_of_intrest'))
			year = int(form.data.get('year'))
			yearly_intrest = 0
			for i in range(0, year*4):
				yearly_intrest = ((amount * rate_of_intrest/100)/4)
				amount = amount + yearly_intrest

			draw = json.dumps({'amount': invested_amount, 'intrest': amount - invested_amount})

	return render(request, 'fd_calc.html', {'draw': draw, 'form': FDForm, 'total_earning': total_earning})