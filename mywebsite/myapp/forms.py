from django import forms

class FDForm(forms.Form):
	"""
	Test
	"""
	amount = forms.IntegerField()
	rate_of_intrest = forms.FloatField()
	year = forms.IntegerField()