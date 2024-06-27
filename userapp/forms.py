from django import forms

from userapp.models import Project, Experience, Qualifications,Certification


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['projectname','description','projectimage']

        widgets = {
            'projectname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the project name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describe the project'}),

        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['companyname','jobrole','duration','responsibility']

        widgets = {
            'companyname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the company name'}),
            'jobrole': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describe the job role'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the duration of work'}),
            'responsibility': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describe the job responsibility'}),

        }

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualifications
        fields = ['qualification','yearofpassing','percentage']

        widgets = {
            'qualification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the qualification'}),
            'yearofpassing': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'year of passing'}),
            'percentage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'percentage'}),
        }


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['certificatename','certificateimage']

        widgets = {
            'certificatename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the certificate name'}),

        }
