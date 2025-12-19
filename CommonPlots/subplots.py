import matplotlib.pyplot as plt
import scipy.stats as stats


class SubPlots:
    def __init__(self, nrows=1, ncols=1, figsize=None):
        # Auto figsize if not provided
        if figsize is None:
            figsize = (4 * ncols, 3 * nrows)

        self.fig, self.axes = plt.subplots(nrows, ncols, figsize=figsize)
        self.index = 0

        # Flatten axes for easy indexing
        if isinstance(self.axes, plt.Axes):
            self.axes = [self.axes]
        else:
            self.axes = self.axes.flatten()

    def _next_ax(self):
        if self.index >= len(self.axes):
            raise IndexError("No subplot slots left.")
        ax = self.axes[self.index]
        self.index += 1
        return ax

    def add_hist(self, x, bins=50):
        ax = self._next_ax()
        ax.hist(x, bins=bins)
        ax.set_title("Histogram")

    def add_probplot(self, x):
        ax = self._next_ax()
        stats.probplot(x, dist="norm", plot=ax)
        ax.set_title("QQ Plot")

    def add_lineplot(self, x, y):
        ax = self._next_ax()
        ax.plot(x, y)
        ax.set_title("Line Plot")

    def add_scatter(self, x, y):
        ax = self._next_ax()
        ax.scatter(x, y)
        ax.set_title("Scatter Plot")

    def show(self):
        plt.tight_layout()
        plt.show()
