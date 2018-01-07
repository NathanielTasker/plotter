from django.db import models


class Plot(models.Model):
    name = models.CharField(max_length=40)
    left = models.CharField(max_length=40)
    right = models.CharField(max_length=40)
    top = models.CharField(max_length=40)
    bottom = models.CharField(max_length=40)
    creation_date = models.DateTimeField()
    def __str__(self):
        return str(self.id) + ': ' + self.name    

class Point(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=6, null=True)
    x = models.IntegerField()
    y = models.IntegerField()
    belong_plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + ' (map' + str(self.belong_plot) + ')'
