import numpy as np
from matplotlib.axes import Axes


def plot_full_custom_2d_grid(
    ax: Axes, 
    basis: np.array, 
    xlim: tuple, 
    ylim: tuple, 
    grid_step: float=1.0, 
    linewidth: float=0.5, 
    color: str = "gray",
):
    grid_lines = []
    
    x = np.arange(xlim[0], xlim[1] + grid_step, grid_step)
    y = np.arange(ylim[0], ylim[1] + grid_step, grid_step)
    
    for xi in x:
        points = np.array([[xi, ylim[0]], [xi, ylim[1]]])
        transformed_points = points @ basis
        line, = ax.plot(transformed_points[:, 0], transformed_points[:, 1], color=color, linestyle='--', linewidth=linewidth)
        grid_lines.append(line)
    
    for yi in y:
        points = np.array([[xlim[0], yi], [xlim[1], yi]])
        transformed_points = points @ basis
        line, = ax.plot(transformed_points[:, 0], transformed_points[:, 1], color=color, linestyle='--', linewidth=linewidth)
        grid_lines.append(line)
    
    return grid_lines


def plot_full_custom_3d_grid(
    ax: Axes, 
    basis: np.array, 
    xlim: tuple, 
    ylim: tuple, 
    zlim: tuple, 
    grid_step: float=1.0, 
    linewidth: float=0.5, 
    color: str = "gray",
    alpha: float = 1.0,
):
    grid_lines = []
    
    x = np.arange(xlim[0], xlim[1] + grid_step, grid_step)
    y = np.arange(ylim[0], ylim[1] + grid_step, grid_step)
    z = np.arange(zlim[0], zlim[1] + grid_step, grid_step)
    
    # Plot lines parallel to x-axis
    for yi in y:
        for zi in z:
            points = np.array([[xlim[0], yi, zi], [xlim[1], yi, zi]])
            transformed_points = points @ basis
            line, = ax.plot(transformed_points[:, 0], transformed_points[:, 1], transformed_points[:, 2], color=color, linestyle='--', linewidth=linewidth, alpha=alpha)
            grid_lines.append(line)
    
    # Plot lines parallel to y-axis
    for xi in x:
        for zi in z:
            points = np.array([[xi, ylim[0], zi], [xi, ylim[1], zi]])
            transformed_points = points @ basis
            line, = ax.plot(transformed_points[:, 0], transformed_points[:, 1], transformed_points[:, 2], color=color, linestyle='--', linewidth=linewidth, alpha=alpha)
            grid_lines.append(line)
    
    # Plot lines parallel to z-axis
    for xi in x:
        for yi in y:
            points = np.array([[xi, yi, zlim[0]], [xi, yi, zlim[1]]])
            transformed_points = points @ basis
            line, = ax.plot(transformed_points[:, 0], transformed_points[:, 1], transformed_points[:, 2], color=color, linestyle='--', linewidth=linewidth, alpha=alpha)
            grid_lines.append(line)
    
    return grid_lines


def cube(return_vertices: bool = False):
    if return_vertices:
        return np.array(
            [
                [0, 0, 0],
                [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0],
                [0, 0, 1],
                [1, 0, 1],
                [1, 1, 1],
                [0, 1, 1],
            ]
        )

    return np.array(
        [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1],
            [0, 0, 1],
            [1, 0, 1],
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 1],
            [0, 1, 1],
            [0, 1, 0]
        ]
    )