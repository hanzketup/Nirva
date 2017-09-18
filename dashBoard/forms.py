from django import forms

class ProfileForm(forms.Form):

    pk = forms.CharField(max_length=4, required=False)

    first = forms.CharField(max_length=60)
    last = forms.CharField(max_length=60)

    nr = forms.CharField(max_length=30)

    gps_lat = forms.CharField(max_length=10, required=False)
    gps_long = forms.CharField(max_length=10, required=False)

    lang = forms.CharField(max_length=5)

    village = forms.CharField(max_length=60, required=False)
    district = forms.CharField(max_length=60, required=False)
    region = forms.CharField(max_length=60, required=False)


class OfferForm(forms.Form):

    name = forms.CharField(max_length=60)
    active = forms.BooleanField()

    expiry = forms.DateTimeField()