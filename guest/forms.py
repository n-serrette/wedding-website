from django import forms

from guest.models import Party, Guest


class PartyRsvp(forms.ModelForm):

    class Meta:
        model = Party
        fields = ['comment']


class GuestRsvp(forms.ModelForm):

    class Meta:
        model = Guest
        fields = ['first_name', 'last_name']


GuestFormset = forms.models.inlineformset_factory(Party, Guest, GuestRsvp,
                                                  extra=0, can_delete=False)


class RsvpCodeForm(forms.Form):
    rsvp_code = forms.CharField(required=True, max_length=6)
