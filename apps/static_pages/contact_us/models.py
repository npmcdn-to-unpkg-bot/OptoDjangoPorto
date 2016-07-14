from django.db import models
import re
from django.core.exceptions import ValidationError

regex = r"([a-zA-Z])"


def validate_even(value):
    if not re.search(regex, value):
        value = str(value)
        output = '%s is not a valid entry' % (str(value))
        raise ValidationError(output)


# Create your models here.
class Contact(models.Model):
    """
    Contact object

    """
    first_name = models.CharField(max_length=50, validators=[validate_even])
    last_name = models.CharField(max_length=50, validators=[validate_even])
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
