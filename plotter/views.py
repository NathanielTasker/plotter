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
        plot_name = request.POST['plot_name']
    else:
        plot_name = None
    left = request.POST['left']
    right = request.POST['right']
    top = request.POST['top']
    bottom = request.POST['bottom']

    new_plot = Plot(name=plot_name, left=left, right=right, top=top, bottom=bottom, creator='@test_creator', creation_date=timezone.now())
    new_plot.save()

    # for point in points:
    #     point_name = request.POST['point_name']
    #     point_color = request.POST['point_color']
    #     point_x = request.POST['point_x']
    #     point_y = request.POST['point_y']
    #     new_plot.point_set.create(name=point_name, color=point_color, x=point_x, y=point_y, belong_plot=new_plot)

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
