import os
import datetime

from django.conf import settings
from django.views.generic.edit import UpdateView, FormView
from django.urls import reverse
from django.templatetags.static import static
from django.contrib import messages


from guest.models import Party
from guest.forms import GuestFormset, PartyRsvp, RsvpCodeForm

from gate.views import get_key, set_key
from gate.mixin import GateLockMixin


class InvitationResponse(GateLockMixin, UpdateView):
    model = Party
    form_class = PartyRsvp
    template_name = "index.html"

    def get_success_url(self):
        return reverse("index")

    def get_object(self, queryset=None):
        obj = self.model.objects.get(
            invitation_number=get_key(self.request))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['guest_formset'] = GuestFormset(self.request.POST,
                                                    instance=self.object)
            context['guest_formset'].full_clean()
        else:
            context['guest_formset'] = GuestFormset(instance=self.object)

        thumbnail_folder = os.path.join(settings.STATIC_ROOT,
                                        "gallery/thumbnail")
        images = os.listdir(
            os.path.join(settings.STATIC_ROOT, "gallery/images"))

        image_list = []
        for img in images:
            name = os.path.basename(img)
            thumbnail = os.path.join(thumbnail_folder, name)
            thumbnail_ulr = static("".join(["gallery/thumbnail/", name]))
            image_url = static("".join(["gallery/images/", name]))
            if os.path.exists(thumbnail):
                image_list.append((image_url, thumbnail_ulr, name))
            else:
                image_list.append((image_url, image_url, name))
        context['gallery_images'] = image_list
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['guest_formset']
        if formset.is_valid():
            response = super().form_valid(form)
            if form.instance.response_received is None:
                form.instance.response_received = datetime.datetime.now()
                form.instance.save()
            formset.instance = self.object
            formset.save()
            messages.success(self.request, 'Votre réponse a bien été enregistré')
            return response
        else:
            return super().form_invalid(form)

    def lock_test_func(self, key):
        obj = Party.objects.get_or_none(invitation_number=key)
        return obj is not None


class GateView(FormView):
    template_name = 'gate.html'
    form_class = RsvpCodeForm

    def form_valid(self, form):
        self.code = form.cleaned_data['rsvp_code']
        set_key(self.request, self.code)
        party = Party.objects.get(invitation_number=self.code)
        if party.invitation_opened is None:
            party.invitation_opened = datetime.datetime.now()
            party.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
