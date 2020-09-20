from django.db import models

from guest.managers import PartyManager, GuestManager


class Party(models.Model):
    """Party model"""
    name = models.CharField(max_length=128)
    invitation_number = models.CharField(max_length=6,
                                         blank=False, unique=True)
    invitation_opened = models.DateTimeField(null=True,
                                             blank=True, default=None)
    response_received = models.DateTimeField(null=True,
                                             blank=True, default=None)
    comment = models.TextField(default="", blank=True)
    invited_dinner = models.BooleanField(default=True)
    invited_brunch = models.BooleanField(default=False)

    objects = PartyManager()

    def __str__(self):
        return self.name

    def has_responded(self):
        return self.response_received is not None

    @property
    def any_guests_attending(self):
        return not self.guest_set.attending().empty()

    @property
    def attending_brunch_count(self):
        return self.guest_set.attending_brunch().count()

    @property
    def attending_dinner_count(self):
        return self.guest_set.attending_dinner().count()

    @property
    def attending_cocktail_count(self):
        return self.guest_set.attending_cocktail().count()


class Guest(models.Model):
    """Guest model"""
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    is_child = models.BooleanField(default=False)
    attending_cocktail = models.BooleanField(default=False)
    attending_dinner = models.BooleanField(default=False)
    attending_brunch = models.BooleanField(default=False)

    objects = GuestManager()
