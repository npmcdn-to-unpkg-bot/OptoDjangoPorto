from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Subscriber(models.Model):
    user = models.OneToOneField(User)
    interest = models.ManyToManyField('partners.BusinessArea')

    def __str__(self):
        return u'{} {}'.format(str(self.user.last_name).upper(), str(self.user.first_name))
