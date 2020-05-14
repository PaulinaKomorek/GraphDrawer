import sys
from services.data_service import DataService
from services.plot_drawing import PlotDrawingService

def main():
    args=sys.argv
    csv=args[1]
    x_column=int(args[2])
    y_columns=list(map(lambda i: int(i), args[3:-1]))
    outname=args[-1]
    with open(csv, "r") as fs:
        ds=DataService(fs.read())
        x_values, y_values=ds.columns(x_column, y_columns)
        plot=PlotDrawingService()
        plot.draw_plot(x_values, y_values, "", "", outname)



if __name__ == "__main__":
    main()