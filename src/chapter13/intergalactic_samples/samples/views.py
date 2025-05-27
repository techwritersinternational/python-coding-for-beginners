from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Sample
from .forms import SampleForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Q
from .forms import SampleSearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Count

def sample_list(request):
    samples = Sample.objects.all()
    form = SampleSearchForm(request.GET)
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        sample_type = form.cleaned_data.get('sample_type')
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')
        
        if query:
            samples = samples.filter(
                Q(sample_id__icontains=query) |
                Q(planet__icontains=query) |
                Q(description__icontains=query)
            )
        
        if sample_type:
            samples = samples.filter(sample_type=sample_type)
        
        if date_from:
            samples = samples.filter(date_collected__gte=date_from)
        
        if date_to:
            samples = samples.filter(date_collected__lte=date_to)
    
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(samples, 10)  # Show 10 samples per page
    
    try:
        samples = paginator.page(page)
    except PageNotAnInteger:
        samples = paginator.page(1)
    except EmptyPage:
        samples = paginator.page(paginator.num_pages)
    
    return render(request, 'samples/sample_list.html', {'samples': samples, 'form': form})

@login_required
def sample_detail(request, pk):
    sample = get_object_or_404(Sample, pk=pk)
    return render(request, 'samples/sample_detail.html', {'sample': sample})

@login_required
def sample_create(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            sample = form.save(commit=False)
            sample.collector = request.user
            sample.save()
            messages.success(request, 'Sample created successfully!')
            return redirect('sample_detail', pk=sample.pk)
    else:
        form = SampleForm()
    return render(request, 'samples/sample_form.html', {'form': form})

@login_required
def sample_update(request, pk):
    sample = get_object_or_404(Sample, pk=pk)
    if request.method == 'POST':
        form = SampleForm(request.POST, instance=sample)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sample updated successfully!')
            return redirect('sample_detail', pk=sample.pk)
    else:
        form = SampleForm(instance=sample)
    return render(request, 'samples/sample_form.html', {'form': form})

@login_required
def sample_delete(request, pk):
    sample = get_object_or_404(Sample, pk=pk)
    if request.method == 'POST':
        sample.delete()
        return redirect('sample_list')
    return render(request, 'samples/sample_confirm_delete.html', {'sample': sample})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sample_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def user_dashboard(request):
    total_samples = Sample.objects.filter(collector=request.user).count()
    sample_types = Sample.objects.filter(collector=request.user).values('sample_type').annotate(count=Count('sample_type'))
    recent_samples = Sample.objects.filter(collector=request.user).order_by('-date_collected')[:5]
    
    context = {
        'total_samples': total_samples,
        'sample_types': sample_types,
        'recent_samples': recent_samples,
    }
    return render(request, 'samples/user_dashboard.html', context)