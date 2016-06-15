from django.db import models

# Create your models here.
class Oled(models.Model):
    opto_part_number = models.CharField(max_length=11)

    def __str__(self):
        return "%s" % (self.opto_part_number)
