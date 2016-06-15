from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Create your views here.


def index(request):
    year_copyright = datetime.now().strftime('%Y')
    year_old = relativedelta(datetime.now(), datetime(1992, 1, 1))
    template = loader.get_template("apps/static_pages/about_us/about_us.html")
    context = {'user': 'anonymous', 'year_copyright': year_copyright, 'year_old': year_old.years}
    return HttpResponse(template.render(context=context, request=request))
