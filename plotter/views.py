from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Plot, Point


def index(request):
    return render(request, 'plotter/index.html')

def plot(request):
    if request.POST['plot_name']:
        plot_name = request.POST['plot_name']
    else:
        plot_name = None
    left = request.POST['left']
    right = request.POST['right']
    top = request.POST['top']
    bottom = request.POST['bottom']

    new_plot = Plot(name=plot_name, left=left, right=right, top=top, bottom=bottom, creation_date=timezone.now())
    new_plot.save()

    for count in range(100):
        point_num = count + 1
        try:
            point_name = request.POST['point_name_%s' % point_num]

            # if request.POST['point_color_%s' % point_num]:
            #     point_color = request.POST['point_color_%s' % point_num]
            # else:
            #     point_color = '000000'
            
            point_x = float(request.POST['point_x_%s' % point_num]) # float() is just for test
            print('point_x is %s' % request.POST['point_x_%s' % point_num]) # just for test
            point_y = float(request.POST['point_y_%s' % point_num]) # float() is just for test
            print('point_y is %s' % request.POST['point_y_%s' % point_num]) # just for test
            
            new_plot.point_set.create(name=point_name, color='000000', x=point_x, y=point_y, belong_plot=new_plot)

        except:
            break

    context = {
        'plot': new_plot,
        'plot_id': new_plot.id,
    }
    return render(request, 'plotter/results.html', context)

def results(request, plot_id):
    plot = Plot.objects.get(pk=plot_id)
    context = {
        'plot': plot,
        'plot_id': plot_id,
    }
    return render(request, 'plotter/results.html', context)

def edit(request, plot_id):
    return HttpResponse("You're editing plot %s." % plot_id)

def posted(request):
    return render(request, 'plotter/posted.html')
