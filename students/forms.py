from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
                "Name": forms.TextInput(attrs={
                    'class': 'form-input',
                    'placeholder': 'Enter your Name'
                }),
                "Course": forms.TextInput(attrs={
                    'class': 'form-text',
                    'placeholder': 'Enter your Course'
                }),
                "image": forms.ClearableFileInput(attrs={
                    'class': 'form-input',
                }),
             }
            
            
        
      