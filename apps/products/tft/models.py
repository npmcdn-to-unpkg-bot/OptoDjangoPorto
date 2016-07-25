from django.db import models


# Create your models here..
class SizeTft(models.Model):
    size_inch = models.FloatField()

    def __str__(self):
        return u"{} \"".format(self.size_inch)

    def _get_size_mm(self):
        # "Returns the size in mm."
        size = round(self.size_inch * 25.4, 2)
        return float(size)

    size_mm = property(_get_size_mm)

    class Meta:
        ordering = ('size_inch',)


class BrandTft(models.Model):
    brand = models.OneToOneField('partners.partner')

    def __str__(self):
        return u"{}".format(self.brand)

    class Meta:
        ordering = ('brand',)


class ResolutionTft(models.Model):
    resolution = models.CharField(max_length=75)
    resolution_x = models.IntegerField()
    resolution_y = models.IntegerField()
    primary_colors = models.CharField(max_length=10, default='RGB')
    ratio = models.CharField(max_length=30)

    def _get_resolution_numeric(self):
        "Returns the resolution YYYxZZZ."
        return u"{} x {} x {}".format(self.resolution_x, self.primary_colors, self.resolution_y)

    resolution_numeric = property(_get_resolution_numeric)

    def __str__(self):
        return u"{} x {} x {} {}".format(self.resolution_x, self.primary_colors, self.resolution_y, self.resolution)

    class Meta:
        ordering = ('resolution_x', 'resolution_y',)


class InterfaceTft(models.Model):
    interface = models.CharField(max_length=75)

    def __str__(self):
        return u"{}".format(self.interface)

    class Meta:
        ordering = ('interface',)


class Tft(models.Model):
    opto_part_number = models.CharField(max_length=11)
    panel_model = models.CharField(max_length=100)

    # Optical properties
    brightness = models.IntegerField()
    contrast = models.CharField(max_length=75)
    colors = models.CharField(max_length=75)
    backlight = models.CharField(max_length=75)
    viewing_angle_upper = models.IntegerField()
    viewing_angle_down = models.IntegerField()
    viewing_angle_left = models.IntegerField()
    viewing_angle_right = models.IntegerField()

    # Dimensions
    outline_x = models.FloatField()
    outline_y = models.FloatField()
    outline_z = models.FloatField()

    active_area_x = models.FloatField()
    active_area_y = models.FloatField()

    # Temperatures
    temperature_operating_min = models.FloatField()
    temperature_operating_max = models.FloatField()
    temperature_storage_min = models.FloatField()
    temperature_storage_max = models.FloatField()

    # Status
    production = models.BooleanField(default=True)

    # Option
    touch_panel = models.BooleanField(default=False)

    # Description
    description = models.CharField(max_length=500)

    # External links
    size = models.ForeignKey(SizeTft, related_name='size_tft')
    brand = models.ForeignKey(BrandTft, related_name='brand_tft')
    resolution = models.ForeignKey(ResolutionTft, related_name='resolution_tft')
    interfaces = models.ManyToManyField(InterfaceTft, related_name='interface_tft')

    def __str__(self):
        return "{} ({})".format(self.panel_model, self.opto_part_number)

    def display_interfaces(self):
        return ', '.join([interface.interface for interface in self.interfaces.all()])

    display_interfaces.short_description = 'Others'
    display_interfaces.allow_tags = True

    class Meta:
        ordering = ('size',)
