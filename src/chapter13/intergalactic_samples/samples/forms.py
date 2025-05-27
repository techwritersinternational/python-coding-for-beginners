from django import forms
from .models import Sample

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['sample_id', 'planet', 'sample_type', 'date_collected', 'description', 'mass']
        widgets = {
            'date_collected': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_mass(self):
        mass = self.cleaned_data['mass']
        if mass <= 0:
            raise forms.ValidationError("Mass must be greater than 0")
        return mass

class SampleSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)
    sample_type = forms.ChoiceField(choices=[('', 'All')] + Sample.SAMPLE_TYPES, required=False)
    date_from = forms.DateField(label='Date from', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(label='Date to', required=False, widget=forms.DateInput(attrs={'type': 'date'}))