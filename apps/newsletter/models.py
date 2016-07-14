from django.db import models
from django.contrib.auth.models import User
from apps.static_pages.partners.models import BusinessArea


# Create your models here.
class Subscriber(models.Model):
    user = models.OneToOneField(User, related_name="person", null=True, blank=True)
    interest = models.ManyToManyField(BusinessArea, related_name='subscriber_interest')
