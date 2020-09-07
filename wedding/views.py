from django.views.generic.edit import FormView
from django.urls import reverse

from guest.forms import RsvpCodeForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = RsvpCodeForm

    def form_valid(self, form):
        self.code = form.cleaned_data['rsvp_code']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('rsvp', kwargs={'rsvp_code': self.code})
