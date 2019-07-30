from django.conf.urls import url
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))

]
