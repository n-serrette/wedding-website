from django import forms

from guest.models import Party, Guest


class PartyRsvp(forms.ModelForm):

    class Meta:
        model = Party
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}),
            }


class GuestRsvp(forms.ModelForm):

    class Meta:
        model = Guest
        fields = ['attending_cocktail', 'attending_dinner', 'attending_brunch']


GuestFormset = forms.models.inlineformset_factory(Party, Guest, GuestRsvp,
                                                  extra=0, can_delete=False)


class RsvpCodeForm(forms.Form):
    rsvp_code = forms.CharField(required=True, max_length=6)

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data['rsvp_code']
        party = Party.objects.get_or_none(invitation_number__iexact=code)
        if party is None:
            self.add_error('rsvp_code', "Numéro d'invitation introuvable")
        return self.cleaned_data
