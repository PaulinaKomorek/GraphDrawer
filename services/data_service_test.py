from data_service import DataService
from plot_drawing import PlotDrawingService

ds=DataService("1 1 2\n2 2 3\n3 3 4\n4 4 5")
x, ys= ds.columns(0,[1,2])
PlotDrawingService().draw_plot(x, ys, "time", "mass", "plot1.png")