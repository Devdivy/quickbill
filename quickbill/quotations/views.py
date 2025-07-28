from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quotation
from .forms import QuotationForm
# Create your views here.

# Create Quotation View
@login_required
def create_quotation(request):
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            quotation = form.save(commit=False)
            quotation.user = request.user
            quotation.save()
            messages.success(request, 'Quotation created successfully.')
            return redirect('quotation_list')
    else:
        form = QuotationForm()
    return render(request, 'quotation/create_quotation.html', {'form': form})

# List View for Quotations
@login_required
def quotation_list(request):
    if request.user.is_superuser:
        quotations = Quotation.objects.all()
    else:
        quotations = Quotation.objects.filter(user=request.user)
    return render(request, 'quotation/quotation_list.html', {'quotations': quotations})

# Detail View for Quotation
@login_required
def quotation_detail(request, pk):
    quotation = get_object_or_404(Quotation, pk=pk)
    if request.user.is_superuser or quotation.user == request.user:
        return render(request, 'quotation/quotation_detail.html', {'quotation': quotation})
    else:
        messages.error(request, 'You do not have permission to view this quotation.')
        return redirect('quotation_list')
    
# Update Quotation View
@login_required
def update_quotation(request,pk):
    quotation = get_object_or_404(Quotation,pk=pk)
    if quotation.user != request.user and not request.user.is_superuser:
        messages.error(request, 'You do not have permission to update this quotation.')
        return redirect('quotation_list')
    
    if request.method == 'POST':
        form = QuotationForm(request.POST, instance=quotation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quotation updated successfully.')
            return redirect('quotation_list')
    else:
        form = QuotationForm(instance=quotation)
    return render(request, 'quotation/update_quotation.html', {'form': form})

@login_required
def delete_quotation(request,pk):
    quotation = get_object_or_404(Quotation, pk=pk)
    if quotation.user != request.user and not request.user.is_superuser:
        return redirect('quotation_list')
    quotation.delete()
    messages.success(request, 'Quotation deleted successfully.')
    return redirect('quotation_list')    
