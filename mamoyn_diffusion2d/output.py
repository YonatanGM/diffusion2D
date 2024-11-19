import matplotlib.pyplot as plt

# function to create a plot for a single timestamp
def create_plot(fig, data, n, dt, T_cold, T_hot, fig_counter):
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(data, cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return im

# function to output all plots as one figure
def output_plots(fig, im, T_cold, T_hot):
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
