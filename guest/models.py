from django.db import models


class Party(models.Model):
    """Party model"""
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Guest(models.Model):
    """Guest model"""
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    is_child = models.BooleanField(default=False)
    attending_ceremony = models.BooleanField(default=False)
    attending_cocktail = models.BooleanField(default=False)
    attending_dinner = models.BooleanField(default=False)
    attending_brunch = models.BooleanField(default=False)
    invited_ceremony = models.BooleanField(default=True)
    invited_cocktail = models.BooleanField(default=True)
    invited_dinner = models.BooleanField(default=True)
    invited_brunch = models.BooleanField(default=True)
    comment = models.TextField(default="")
