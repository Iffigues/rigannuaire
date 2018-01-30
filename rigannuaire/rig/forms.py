from django import forms
from django.forms import ModelForm, TextInput, EmailInput

GENDER_TYPE = (
    ('','Gender'),
    ('m', 'man'),
    ('f', 'woman'),
)


class ContactForm(forms.Form):
    fname = forms.CharField(
        label='fname',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Firstname'}),
        required=False
    )
    lname = forms.CharField(
        label='lname',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Lastname'}),
        required=False
    )

    email = forms.EmailField(
        label='email',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
        required=False
    )
    snbr = forms.CharField(
        label='snbr',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Street Number'}),
        required=False
    )
    sn = forms.CharField(
        label='sn',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Street Name'}),
        required=False
    )
    st = forms.EmailField(
        label='st',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Street Type'}),
        required=False
    )
    city = forms.CharField(
        label='city',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'City'}),
        required=False
    )
    sigle = forms.CharField(
        label='sigle',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Sigle'}),
        required=False
    )
    zips = forms.CharField(
        label='zips',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'ZIP'}),
        required=False
    )
    gender = forms.CharField(
        label='gender',
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Gender'}),
    )
    tel = forms.CharField(
        label='tel',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phone'}),
        required=False
    )
    gender = forms.ChoiceField(
        label='gender',
        required=False,
    #    widget=forms.HiddenInput(),
        choices=GENDER_TYPE,
    )
    
    pass
