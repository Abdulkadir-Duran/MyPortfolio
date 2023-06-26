from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Name:', widget=forms.TextInput(attrs={'placeholder':"your Name"}), required=True)
    email = forms.EmailField(max_length=100, label='Email:', widget=forms.EmailInput(attrs={'placeholder':"Your Email address"}), required=True)
    subject = forms.CharField(max_length=150, label='Subject', widget=forms.TextInput(attrs={'placeholder':"your Email Subject"}), required=True)
    message = forms.CharField(max_length=1000, label='Message', widget=forms.Textarea(attrs={'placeholder':"Write your message here",'cols': 5, 'rows': 3
    
    }), required=True)