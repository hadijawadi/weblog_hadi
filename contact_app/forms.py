from django import forms
from .models import Contact

class Contact_form(forms.ModelForm):
      class Meta:
        model =Contact
        fields = ('full_name','email','message',)
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
        }
        def clean(self):
            cleaned_data = super().clean()
            message = cleaned_data.get('message')
            full_name = cleaned_data.get('full_name')

            if  full_name == '':
               
                    raise forms.ValidationError("please fill the form ")
            return cleaned_data
        
    
    
  