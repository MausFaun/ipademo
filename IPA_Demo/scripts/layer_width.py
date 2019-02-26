from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display
layer_width = []

def f1(x=2):
    return x

def query_layer_width(depth):
    style = {'description_width': 'initial'}
    for layer in range(depth.value):
        layer_width.append(widgets.IntSlider(
            value=2,
            min=1,
            max=512,
            step=1,
            description='Width Layer {}:'.format(layer+1),
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=True,
            readout_format='d',
            style=style
        ))
    return layer_width