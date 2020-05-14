import matplotlib.pyplot as plt

class PlotDrawingService:

    def draw_plot(self, x: list, ys: list, labelx: str, labely: str, filename: str):
        for y in ys:
            plt.plot(x, y)
        plt.ylabel(labely)
        plt.xlabel(labelx)
        plt.savefig(filename)
        plt.clf()
   