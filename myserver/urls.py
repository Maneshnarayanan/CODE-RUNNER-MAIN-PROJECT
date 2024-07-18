from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^math/',views.sathar,name='sathar'),
    url(r'^compile/',views.compile,name='compile'),
    url(r'^call/',views.call,name='call'),
    url(r'^recall/',views.recall,name='recall')
    
    

]