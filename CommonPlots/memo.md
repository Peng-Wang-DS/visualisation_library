# usage example

'''assume the project root is parent of visualisation_lib'''

from visualisation_lib.CommonPlots.subplots import SubPlots
import numpy as np

x = np.random.randn(1000)
y = np.random.randn(1000)

sp = SubPlots(nrows=4, ncols=2)  

sp.add_hist(x)
sp.add_probplot(x)
sp.add_lineplot(np.arange(len(x)), x)
sp.add_scatter(x, y)
sp.add_probplot(x)
sp.add_lineplot(np.arange(len(x)), x)
sp.add_scatter(x, y)
sp.show()