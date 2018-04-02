from django.conf.urls import *
from . import views # import views so we can use them in urls.
app_name="rig"
urlpatterns = [
    url(r'^$', views.index,name='rig'),# "/store" will call the method "index" in "views.py"
    url(r'^s/$', views.search,name='s'), # "/store" will call the method "index" in "views.py"
    url(r'^s/id/(?P<ids>\w{0,50})/$', views.ids),
    url(r'^a/$', views.annuaire,name='a'),
    url(r'^a/(?P<odn>\w{0,50})/$', views.annuaires),
    url(r'^a/(?P<odn>\w{0,50})/(?P<idn>[\w \, \- \% \_ \( \) ]+)/$', views.anu),
]
