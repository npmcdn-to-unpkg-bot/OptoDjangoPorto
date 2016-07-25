from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.utils.translation import get_language
# for translations
from django.utils.translation import ugettext_lazy as _


# Create your views here.


# def index(request):
    # Translators : This message is a test message.
    #  output = _("Hello")
    # return HttpResponse(output)

def index(request):
    print(get_language())
    year_copyright = datetime.now().strftime('%Y')
    template = loader.get_template('apps/static_pages/landing_page/index.html')
    context = {'user': 'anonymous', 'year_copyright': year_copyright}
    return HttpResponse(template.render(context=context, request=request))
