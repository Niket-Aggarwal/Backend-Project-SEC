from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    endtime = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    class Meta:
        model = Booking
        fields = ['date', 'time', 'endtime','no_of_people', 'specification']