#yfrom django.conf.urls import url
from django.urls import path
from polls import views as view

urlpatterns = [
    # ex : /polls/
#    url(r'^$', view.index, name='index'),
    path ('$', view.index, name='index'),
    # ex : /polls/5/
    path('(?P<question_id>[0-9]+)/$',view.detail, name= 'detail'),
    #url(r'^(?P<question_id>[0-9]+)/$', view.detail, name='detail'),
    # ex : /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', view.results, name='results'),
    path('(?P<question_id>[0-9]+)/results/$', view.results, name= 'results'),
    # ex : /polls/5/vote
    #url(r'^(?P<question_id>[0-9]+)/vote/$', view.vote, name='vote'),
    path('(?P<question_id>[0-9]+)/vote/$',view.vote, name= 'vote'),
]