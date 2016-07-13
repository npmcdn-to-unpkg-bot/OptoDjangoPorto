from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from.models import Partner, BusinessArea


# Create your views here.


def index(request):
    year_copyright = datetime.now().strftime('%Y')
    template = loader.get_template('apps/static_pages/partners/partners.html')
    partners = Partner.objects.all()
    areas = BusinessArea.objects.all()
    context = {'user': 'anonymous', 'year_copyright': year_copyright, 'partners' : partners, 'areas': areas }
    return HttpResponse(template.render(context=context, request=request))
