from django.db import models
from django.db.models import Q

from django.core.exceptions import ObjectDoesNotExist


class GetOrNoneManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None


class PartyQuerySet(models.QuerySet):
    def opened(self):
        return self.exclude(invitation_opened=None)

    def unopened(self):
        return self.filter(invitation_opened=None)

    def answered(self):
        return self.exclude(response_received=None)

    def unanswered(self):
        return self.filter(response_received=None)


class GuestQuerySet(models.QuerySet):
    def attending_dinner(self):
        return self.filter(attending_dinner=True)

    def attending_cocktail(self):
        return self.filter(attending_cocktail=True)

    def attending_brunch(self):
        return self.filter(attending_brunch=True)

    def child(self):
        return self.filter(is_child=True)

    def attending(self):
        return self.filter(
            Q(attending_cocktail=True)
            | Q(attending_brunch=True)
            | Q(attending_dinner=True))

    def not_attending(self):
        return self.filter(
            Q(attending_cocktail=False)
            | Q(attending_brunch=False)
            | Q(attending_dinner=False)).exclude(party__response_received=None)


PartyManager = GetOrNoneManager.from_queryset(PartyQuerySet)
GuestManager = GetOrNoneManager.from_queryset(GuestQuerySet)
