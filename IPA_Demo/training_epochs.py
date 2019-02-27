from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display

def f1(x=2):
    return x

def query_training_epochs():
    style = {'description_width': 'initial'}
    training_epochs = widgets.IntSlider(
        value=3,
        min=1,
        max=100,
        step=1,
        description='Training epochs:',
        disabled=False,
        continuous_update=True,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        style=style
    )
    return training_epochs