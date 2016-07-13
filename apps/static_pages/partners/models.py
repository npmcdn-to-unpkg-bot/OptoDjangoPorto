from django.db import models


# Create your models here.
class BusinessArea(models.Model):
    area = models.CharField(max_length=200)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return u"{}".format(self.area)


class Partner(models.Model):
    name = models.CharField(max_length=75)
    logo = models.ImageField()
    area = models.ManyToManyField(BusinessArea, related_name='business_area_partner')

    def __str__(self):
        return u"{}".format(self.name)

    def get_area(self):
        return self.area.all()

    class Meta:
        ordering = ('name',)
