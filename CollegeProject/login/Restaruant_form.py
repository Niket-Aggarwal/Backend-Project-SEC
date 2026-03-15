from django import forms
from .models import Restaurant

class RestaurantSignupStep1Form(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ["restaurant_name","password","phone_number","address"]
        widgets = {
            "restaurant_name": forms.TextInput(attrs={
                "placeholder": "Restaurant Name"
            }),
            "password": forms.PasswordInput(attrs={
                "placeholder": "Password"
            }),
            "phone_number": forms.TextInput(attrs={
                "placeholder": "Phone Number"
            }),
            "address": forms.Textarea(attrs={
                "placeholder": "Address",
                "rows": 2
            }),
        }

class RestaurantSignupStep2Form(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ["pincode","total_gathering","specification","description","photo1","photo2","photo3","photo4","photo5"]
        widgets = {
            "pincode": forms.TextInput(attrs={
                "placeholder": "Pincode"
            }),
            "total_gathering": forms.NumberInput(attrs={
                "placeholder": "Total Gathering Capacity"
            }),
            "specification": forms.TextInput(attrs={
                "placeholder": "Specification (Veg/ Special Cousine or any)"
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Restaurant Description",
                "rows": 4
            }),
        }

class RestrauntSigninForm(forms.Form):
    restaurant_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Restaurant Name"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password"
        })
    )