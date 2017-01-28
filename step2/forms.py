import re
from django import forms
class NameForm(forms.Form):
    book_name = forms.CharField(label='Book Title', max_length=30)
    price = forms.CharField(label='Price', max_length=5)
    user = forms.CharField(label='Your Name', max_length=100)
    phone = forms.CharField(label='Your phone number', max_length=30)