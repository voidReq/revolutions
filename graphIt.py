import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import numpy.ma as ma  # For masking arrays


def graphIt(equation, radialDisplacement, x1, x2, y1, y2, z1, z2, W, Y, Z, axis):
    x_max = np.max(W)
    x_min = np.min(W)
    y_max = np.max(Y)
    y_min = np.min(Y)
    z_max = np.max(Z)
    z_min = np.min(Z)

    # Uses whichever bounds are larger
    ax_x_min = max(x_min, x1)
    ax_x_max = min(x_max, x2)
    ax_y_min = max(y_min, y1)
    ax_y_max = min(y_max, y2)
    ax_z_min = max(z_min, z1)
    ax_z_max = min(z_max, z2)

    fig = plt.figure(figsize=(11, 11))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(W, Y, Z, rstride=5, cstride=5, cmap='viridis', edgecolor='none', alpha=0.8)

    # Axis limits of graph set
    ax.set_xlim(ax_x_min, ax_x_max)
    ax.set_ylim(ax_y_min, ax_y_max)
    ax.set_zlim(ax_z_min, ax_z_max)

    # not my code
    ax.set_box_aspect([1, (y2 - y1) / (x2 - x1), (z2 - z1) / (x2 - x1)])

    # Dynamic labels and title
    ax.set_title(f"Revolution of ${sp.latex(equation)}$ around {axis}={radialDisplacement}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # not me
    W_masked = ma.masked_outside(W, ax_x_min, ax_x_max)
    Y_masked = ma.masked_outside(Y, ax_y_min, ax_y_max)
    Z_masked = ma.masked_where(
        (W_masked.mask | Y_masked.mask) | (Z < ax_z_min) | (Z > ax_z_max), Z
    )

    # Use the masked arrays for plotting
    ax.plot_surface(W_masked, Y_masked, Z_masked, rstride=5, cstride=5, cmap='viridis', edgecolor='none', alpha=0.8)

    # stackoverflow code, I didn't handle a lot of the masking
    def zoom(event):
        nonlocal ax_x_min, ax_x_max, ax_y_min, ax_y_max, ax_z_min, ax_z_max
        zoom_factor = 0.1  # Adjust zoom sensitivity

        if event.step > 0:  # Zoom in
            factor = 1 - zoom_factor
        elif event.step < 0:  # Zoom out
            factor = 1 + zoom_factor
        else:
            return

        center_x = (ax_x_min + ax_x_max) / 2
        center_y = (ax_y_min + ax_y_max) / 2
        center_z = (ax_z_min + ax_z_max) / 2

        ax_x_min = center_x + (ax_x_min - center_x) * factor
        ax_x_max = center_x + (ax_x_max - center_x) * factor
        ax_y_min = center_y + (ax_y_min - center_y) * factor
        ax_y_max = center_y + (ax_y_max - center_y) * factor
        ax_z_min = center_z + (ax_z_min - center_z) * factor
        ax_z_max = center_z + (ax_z_max - center_z) * factor

        # remask data
        W_masked = ma.masked_outside(W, ax_x_min, ax_x_max)
        Y_masked = ma.masked_outside(Y, ax_y_min, ax_y_max)
        Z_masked = ma.masked_where(
            (W_masked.mask | Y_masked.mask) | (Z < ax_z_min) | (Z > ax_z_max), Z
        )

        ax.cla()  # clear
        ax.plot_surface(W_masked, Y_masked, Z_masked, rstride=5, cstride=5, cmap='viridis', edgecolor='none', alpha=0.8)
        # redraw

        # Update limits
        ax.set_xlim(ax_x_min, ax_x_max)
        ax.set_ylim(ax_y_min, ax_y_max)
        ax.set_zlim(ax_z_min, ax_z_max)

        # update titles each time
        ax.set_title(f"Surface of Revolution of ${sp.latex(equation)}$ Around the X={radialDisplacement}")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        fig.canvas.draw_idle()

    # Connect the zoom function to the figure
    fig.canvas.mpl_connect('scroll_event', zoom)

    # Show the plot
    plt.ion()
    plt.show()
