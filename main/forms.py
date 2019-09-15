from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="Name", max_length= 30, required=True, help_text="Enter Name" )
    email = forms.EmailField(label="Email", required=True, help_text="Enter Email")
    phone = forms.CharField(label="Phone", max_length= 12, required=True, help_text="Phone")