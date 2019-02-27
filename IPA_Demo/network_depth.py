from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display

def f1(depth=2):
    return depth
    
def query_network_depth():
    style = {'description_width': 'initial'}
    depth = widgets.IntSlider(
        value=2,
        min=1,
        max=8,
        step=1,
        description='Network depth:',
        disabled=False,
        continuous_update=True,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        style=style
    )
    return depth