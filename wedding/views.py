import os
from django.views.generic.edit import FormView
from django.urls import reverse
from django.conf import settings
from django.templatetags.static import static

from guest.forms import RsvpCodeForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = RsvpCodeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        self.code = form.cleaned_data['rsvp_code']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('rsvp', kwargs={'rsvp_code': self.code})
