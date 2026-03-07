from django import forms
from .models import User


class CustomerSignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "password", "phone_number", "pincode"]

        widgets = {
            "username": forms.TextInput(attrs={
                "placeholder": "Username"
            }),

            "password": forms.PasswordInput(attrs={
                "placeholder": "Password"
            }),

            "phone_number": forms.TextInput(attrs={
                "placeholder": "Phone no."
            }),

            "pincode": forms.TextInput(attrs={
                "placeholder": "Pincode"
            })
        }


class CustomerSigninForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Username"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password"
        })
    )