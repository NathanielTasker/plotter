from django.conf.urls import url

from . import views

app_name = 'plotter'
urlpatterns = [
    # ex: /plotter/
    url(r'^$', views.index, name='index'),
    # ex: /plotter/plot/
    url(r'^plot/$', views.plot, name='plot'),
    # ex: /plotter/plot_5/results/
    url(r'^plot_(?P<plot_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /plotter/plot_5/edit/
    url(r'^plot_(?P<plot_id>[0-9]+)/edit/$', views.edit, name='edit'),
    # ex: /plotter/posted/
    url(r'^posted/$', views.posted, name='posted'),
]
