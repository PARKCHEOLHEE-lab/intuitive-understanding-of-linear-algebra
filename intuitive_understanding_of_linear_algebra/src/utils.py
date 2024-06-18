import numpy as np
from matplotlib.axes import Axes


def plot_full_custom_2d_grid(ax: Axes, basis: np.array, xlim: tuple, ylim: tuple, grid_step: float=1.0):
    
    x = np.arange(xlim[0], xlim[1] + grid_step, grid_step)
    y = np.arange(ylim[0], ylim[1] + grid_step, grid_step)
    
    for xi in x:
        points = np.array([[xi, ylim[0]], [xi, ylim[1]]])
        transformed_points = points @ basis
        ax.plot(transformed_points[:, 0], transformed_points[:, 1], color='gray', linestyle='--', linewidth=0.5)
    
    for yi in y:
        points = np.array([[xlim[0], yi], [xlim[1], yi]])
        transformed_points = points @ basis
        ax.plot(transformed_points[:, 0], transformed_points[:, 1], color='gray', linestyle='--', linewidth=0.5)
        