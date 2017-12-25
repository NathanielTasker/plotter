from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Plot, Point


def index(request):
    print('index is called!') #for test
    return render(request, 'plotter/index.html')

def plot(request):
    print('plot is called') #for test
    if request.POST['plot_name']:
        plot_name = str(request.POST['plot_name'])
    else:
        plot_name = None
    left = str(request.POST['left'])
    right = str(request.POST['right'])
    top = str(request.POST['top'])
    bottom = str(request.POST['bottom'])

    new_plot = Plot(name=plot_name, left=left, right=right, top=top, bottom=bottom, creator='@test_creator', creation_date=timezone.now())
    new_plot.save()

    context = {
        'map_id': new_plot.id,
    }
    return render(request, 'plotter/results.html', context)

def results(request, plot_id):
    context = {
        'plot_id': plot_id,
    }
    return render(request, 'plotter/results.html', context)

def edit(request, plot_id):
    return HttpResponse("You're editing plot %s." % plot_id)

def posted(request):
    return render(request, 'plotter/posted.html')
