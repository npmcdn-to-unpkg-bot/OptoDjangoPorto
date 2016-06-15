from django.shortcuts import render
from django.views import generic

from .models import Tft, SizeTft
# Create your views here.

def IndexView(request):
        tft_list_all = Tft.objects.order_by('size')
        tft_size = SizeTft.objects.order_by('size_inch')


        template_name = 'templates/apps/products/tft/tft_landing.html'
        context = {
            'tft_list_all': tft_list_all,
            'tft_size': tft_size,
        }
        return render(request, template_name, context)


class IndexViewAll(generic.ListView):
    template_name = 'templates/apps/products/tft/index_all.html'
    context_object_name = 'complet_list_of_tfts'

    def get_queryset(self):
        """Return the list of tfts."""
        return Tft.objects.order_by('size')


class IndexViewProd(generic.ListView):
    template_name = 'templates/apps/products/tft/index_production.html'
    context_object_name = 'complet_list_of_tfts_in_production'

    def get_queryset(self):
        """Return the list of tfts."""
        return Tft.objects.filter(production=True).order_by('size')


class IndexViewObsolete(generic.ListView):
    template_name = 'templates/apps/products/tft/index_obsolete.html'
    context_object_name = 'complet_list_of_tfts_are_obsolete'

    def get_queryset(self):
        """Return the list of tfts."""
        return Tft.objects.filter(production=False).order_by('size')

class DetailView(generic.DetailView):
    model = Tft
    template_name = 'templates/apps/products/tft/details.html'