from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="Name", max_length= 30, required=True, help_text="Who are you?" )
    email = forms.EmailField(label="Email", required=True, help_text="Trust me, I won't spam you with emails.")
    phone = forms.CharField(label="Phone", max_length= 12, required=True, help_text="I follow the policy 'text first, call later'")
    message = forms.CharField(label = "Message",  widget=forms.Textarea, help_text='Leave me a message!')