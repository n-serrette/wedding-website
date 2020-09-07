from django.urls import path

from . import views

urlpatterns = [
    path('rsvp/<rsvp_code>',
         views.InvitationResponse.as_view(), name='rsvp'),
]
