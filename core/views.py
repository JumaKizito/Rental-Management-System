from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Property
from .forms import PropertyForm

@login_required
def dashboard_view(request):
    return render(request, 'core/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'core/property_list.html', {
        'properties': properties
    })


@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()

    return render(request, 'core/property_form.html', {
        'form': form,
        'title': 'Add Property'
    })


@login_required
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'core/property_detail.html', {
        'property': property
    })


@login_required
def property_update(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_detail', pk=pk)
    else:
        form = PropertyForm(instance=property)

    return render(request, 'core/property_form.html', {
        'form': form,
        'title': 'Edit Property'
    })


@login_required
def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.method == 'POST':
        property.delete()
        return redirect('property_list')

    return render(request, 'core/property_confirm_delete.html', {
        'property': property
    })
