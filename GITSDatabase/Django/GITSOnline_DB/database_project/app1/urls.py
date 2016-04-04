from django.conf.urls import url

from . import views

app_name = 'app1'
urlpatterns = [
    # ex: /app1/
    url(r'^$', views.index, name='index'),
    # the 'name' value as called by the {% url %} template tag
    # ex: /app1/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /app1/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /app1/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
