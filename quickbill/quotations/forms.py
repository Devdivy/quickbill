from django import forms
from .models import Quotation

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields =['client_name',  'project_title', 'client_email', 'description', 'amount']
        