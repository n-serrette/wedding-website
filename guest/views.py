from django.views.generic.edit import UpdateView
from django.urls import reverse

from guest.models import Party
from guest.forms import GuestFormset


class InvitationResponse(UpdateView):
    model = Party
    fields = ['comment']
    template_name = "form.html"

    def get_success_url(self):
        return reverse("index")

    def get_object(self, queryset=None):
        obj = self.model.objects.get(
            invitation_number=self.kwargs.get("rsvp_code", None))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['guest_formset'] = GuestFormset(self.request.POST,
                                                    instance=self.object)
            context['guest_formset'].full_clean()
        else:
            context['guest_formset'] = GuestFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['guest_formset']
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)
