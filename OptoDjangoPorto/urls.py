"""OptoDjangoPorto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.static_pages.landing_page.urls')),
    url(r'^about-us/', include('apps.static_pages.about_us.urls')),
    url(r'^contact-us/', include('apps.static_pages.contact_us.urls')),
    url(r'^tft/', include('apps.products.tft.urls', namespace="tft")),
    url(r'^lcd/', include('apps.products.lcd.urls')),
    url(r'^oled/', include('apps.products.oled.urls')),
    url(r'^epaper/', include('apps.products.epaper.urls')),
    url(r'^custom/', include('apps.products.custom.urls')),
    url(r'^panel_printers/', include('apps.products.thermal_printers.panel_printers.urls')),
    url(r'^mobile_printers/', include('apps.products.thermal_printers.mobile_printers.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [url(r'^uml/', include('django_spaghetti.urls'))]

