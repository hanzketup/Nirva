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

    pk = forms.CharField(max_length=10)

    name = forms.CharField(max_length=60)
    active = forms.CharField(max_length=10)

    expiry = forms.CharField(required=False)
    message = forms.CharField(max_length=300,required=False)
    unit = forms.CharField(max_length=50, required=False)


class InterestForm(forms.Form):

    pk = forms.CharField(max_length=10)
    name = forms.CharField(max_length=60)


class GroupForm(forms.Form):
    pk = forms.CharField(max_length=4, required=False)

    address = forms.CharField(max_length=60, required=False)
    village = forms.CharField(max_length=60, required=False)
    district = forms.CharField(max_length=60, required=False)
    region = forms.CharField(max_length=60, required=False)