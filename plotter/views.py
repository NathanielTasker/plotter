from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Plot, Point

from mpl_toolkits.axes_grid.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np


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

    points = []
    points_x = []
    points_y = []

    for count in range(100):
        point_num = count + 1
        try:
            points.append(request.POST['point_name_%s' % point_num])
            points_x.append(float(request.POST['point_x_%s' % point_num]) - 300) # float() is just for test
            points_y.append(300 - float(request.POST['point_y_%s' % point_num])) # float() is just for test
        except:
            break

    if 1:
        fig = plt.figure(1)
        ax = SubplotZero(fig, 111)
        fig.add_subplot(ax)

        for direction in ["xzero", "yzero"]:
            ax.axis[direction].set_visible(True)

        for direction in ["left", "right", "bottom", "top"]:
            ax.axis[direction].set_visible(False)

    plt.scatter(points_x, points_y)
    for point, x, y in zip(points, points_x, points_y):
        plt.annotate(point, xy=(x, y), xytext=(5, -5), textcoords='offset points')

    plt.gca().set_xlim([0, 600])
    plt.gca().set_ylim([0, 600])
    plt.axis("equal")
    plt.xlabel('%s - %s' % (left, right), fontdict={'family': 'Arial'})
    plt.ylabel('%s - %s' % (bottom, top), fontdict={'family': 'Arial'})
    plt.title(plot_name)

    plt.show()

    # context = {
    #     'plot': new_plot,
    #     'plot_id': new_plot.id,
    # }
    # return render(request, 'plotter/results.html', context)

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
