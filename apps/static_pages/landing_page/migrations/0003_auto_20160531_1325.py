# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_auto_20160531_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShowcaseSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('master_speed', models.IntegerField(default=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/media/revolution-slider/%Y/%m/%d')),
                ('transition', models.CharField(choices=[('random-static', 'Random static'), ('slideup', 'Slide To Top'), ('slidedown', 'Slide To Bottom'), ('slideright', 'Slide To Right'), ('slideleft', 'Slide To Left'), ('slidehorizontal', 'Slide Horizontal (depending on Next/Previous)'), ('slidevertical', 'Slide Vertical (depending on Next/Previous)'), ('boxslide', 'Slide Boxes'), ('slotslide-horizontal', 'Slide Slots Horizontal'), ('slotslide-vertical', 'Slide Slots Vertical'), ('boxfade', 'Fade Boxes'), ('slotfade-horizontal', 'Fade Slots Horizontal'), ('slotfade-vertical', 'Fade Slots Vertical'), ('fadefromright', 'Fade and Slide from Right'), ('fadefromleft', 'Fade and Slide from Left'), ('fadefromtop', 'Fade and Slide from Top'), ('fadefrombottom', 'Fade and Slide from Bottom'), ('fadetoleftfadefromright', 'Fade To Left and Fade From Right'), ('fadetorightfadefromleft', 'Fade To Right and Fade From Left'), ('fadetotopfadefrombottom', 'Fade To Top and Fade From Bottom'), ('fadetobottomfadefromtop', 'Fade To Bottom and Fade From Top'), ('parallaxtoright', 'Parallax to Right'), ('parallaxtoleft', 'Parallax to Left'), ('parallaxtotop', 'Parallax to Top'), ('parallaxtobottom', 'Parallax to Bottom'), ('scaledownfromright', 'Zoom Out and Fade From Right'), ('scaledownfromleft', 'Zoom Out and Fade From Left'), ('scaledownfromtop', 'Zoom Out and Fade From Top'), ('scaledownfrombottom', 'Zoom Out and Fade From Bottom'), ('zoomout', 'ZoomOut'), ('zoomin', 'ZoomIn'), ('slotzoom-horizontal', 'Zoom Slots Horizontal'), ('slotzoom-vertical', 'Zoom Slots Vertical'), ('fade', 'Fade'), ('random', 'Random Flat and Premium')], default=('random-static', 'Random static'), max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MainShowcaseSlideLayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField(default=1000, help_text='The timepoint in ms at which the layer should move in to the slide.')),
                ('end', models.IntegerField(blank=True, default=2500, help_text='The timepoint in ms at which the layer should move out from the slide.', null=True)),
                ('speed', models.IntegerField(blank=True, default=100, help_text='The speed in ms of the transition to move the layer in the slide at the defined timepoint.', null=True)),
                ('position_x', models.CharField(default='center', help_text="Possible values are 'left', 'center', 'right', or any Value between -2500  and 2500.", max_length=255)),
                ('position_y', models.CharField(default='center', help_text="Possible Values are 'top', 'center', 'bottom', or any Value between -2500 and 2500.", max_length=255)),
                ('v_offset', models.IntegerField(default=0, help_text='value in pixels', verbose_name='Vertical offset')),
                ('h_offset', models.IntegerField(default=0, help_text='value in pixels', verbose_name='Horizontal offset')),
                ('incoming_animation', models.CharField(blank=True, choices=[('', 'None'), ('sft', 'Short from Top'), ('sfb', 'Short from Bottom'), ('sfr', 'Short from Right'), ('sfl', 'Short from Left'), ('lft', 'Long from Top'), ('lfb', 'Long from Bottom'), ('lfr', 'Long from Right'), ('lfl', 'Long from Left'), ('skewfromleft', 'Skew from Left'), ('skewfromright', 'Skew from Right'), ('skewfromleftshort', 'Skew Short from Left'), ('skewfromrightshort', 'Skew Short from Right'), ('fade', 'fading'), ('randomrotate', 'Fade in, Rotate from a Random position and Degree')], default=('', 'None'), max_length=255)),
                ('outgoing_animation', models.CharField(blank=True, choices=[('', 'None'), ('stt', 'Short to Top'), ('stb', 'Short to Bottom'), ('str', 'Short to Right'), ('stl', 'Short to Left'), ('ltt', 'Long to Top'), ('ltb', 'Long to Bottom'), ('ltr', 'Long to Right'), ('ltl', 'Long to Left'), ('skewtoleft', 'Skew to Left'), ('skewtoright', 'Skew to Right'), ('skewtoleftshort', 'Skew Short to Left'), ('skewtorightshort', 'Skew Short to Right'), ('fadeout', 'fading'), ('randomrotateout', 'Fade in, Rotate from a Random position and Degree')], default=('', 'None'), max_length=255)),
                ('easing', models.CharField(choices=[('OutBack', 'easeOutBack'), ('InQuad', 'easeInQuad'), ('OutQuad', 'easeOutQuad'), ('InOutQuad', 'easeInOutQuad'), ('InCubic', 'easeInCubic'), ('OutCubic', 'easeOutCubic'), ('InOutCubic', 'easeInOutCubic'), ('InQuart', 'easeInQuart'), ('OutQuart', 'easeOutQuart'), ('InOutQuart', 'easeInOutQuart'), ('InQuint', 'easeInQuint'), ('OutQuint', 'easeOutQuint'), ('InOutQuint', 'easeInOutQuint'), ('InSine', 'easeInSine'), ('OutSine', 'easeOutSine'), ('InOutSine', 'easeInOutSine'), ('InExpo', 'easeInExpo'), ('OutExpo', 'easeOutExpo'), ('InOutExpo', 'easeInOutExpo'), ('InCirc', 'easeInCirc'), ('OutCirc', 'easeOutCirc'), ('InOutCirc', 'easeInOutCirc'), ('InElastic', 'easeInElastic'), ('OutElastic', 'easeOutElastic'), ('InOutElastic', 'easeInOutElastic'), ('InBack', 'easeInBack'), ('OutBack', 'easeOutBack'), ('InOutBack', 'easeInOutBack'), ('InBounce', 'easeInBounce'), ('OutBounce', 'easeOutBounce'), ('InOutBounce', 'easeInOutBounce')], default=('OutBack', 'easeOutBack'), max_length=25)),
                ('layer_text', models.TextField(blank=True, max_length=255)),
                ('splitin', models.CharField(blank=True, choices=[('', "Don't split"), ('chars', 'Characters'), ('words', 'Words'), ('lines', 'Lines')], default=('', "Don't split"), max_length=255)),
                ('splitout', models.CharField(blank=True, choices=[('', "Don't split"), ('chars', 'Characters'), ('words', 'Words'), ('lines', 'Lines')], default=('', "Don't split"), max_length=255)),
                ('elementdelay', models.FloatField(blank=True, default=0, help_text="A Value between 0 and 1 to make delays between the 'splitted text element' start animation.", null=True)),
                ('endelementdelay', models.FloatField(blank=True, default=0, help_text="A Value between 0 and 1 to make delays between the 'splitted text element' end animation.", null=True)),
                ('style', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='MainShowcase',
        ),
        migrations.DeleteModel(
            name='MainShowcaseLayer',
        ),
        migrations.DeleteModel(
            name='SecondaryShowcase',
        ),
    ]
