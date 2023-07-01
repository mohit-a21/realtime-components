import matplotlib.pyplot as plt

from models import ColorPallet, FreeformColorPallet


def add_rectangle(ax, heading, color):
    ax.axis('off')
    ax.set_title("{heading}: {color}".format(heading=heading, color=color))
    ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=color))


def generate_color_boxes(color_pallet: ColorPallet):
    num_colors = 5
    fig, ax = plt.subplots(1, num_colors, figsize=(12, 2))

    add_rectangle(ax[0], 'text', color_pallet.text)
    add_rectangle(ax[1], 'background', color_pallet.background)
    add_rectangle(ax[2], 'primary', color_pallet.primary)
    add_rectangle(ax[3], 'secondary', color_pallet.secondary)
    add_rectangle(ax[4], 'accent', color_pallet.accent)

    plt.show()


def generate_freeform_color_boxes(color_pallet: FreeformColorPallet):
    colors = color_pallet.colors
    num_colors = len(colors)
    fig, ax = plt.subplots(1, num_colors, figsize=(12, 2))

    for idx, color in enumerate(colors):
        add_rectangle(ax[idx], f'{idx}', color)

    plt.show()
