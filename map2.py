#%%

import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


shapefile = "C:/Users/Tobias/Desktop/summerproject/code/test/data/vg250_3112.utm32s.shape.ebenen/vg250_ebenen"
map_complete = gpd.read_file(shapefile)


head = map_complete.head()
shape = map_complete.shape
# list(map_complete.columns)
    
# print(head)
# print(shape)

## create a mapfile that is Bundesländer only
map_complete["Bundesland"] = map_complete["RS"].str[0:2]
step1 = map_complete[["Bundesland", "geometry"]]
Bundeslaender = map_complete.dissolve(by="Bundesland")

## create a mapfile that is Kreise only
map_complete["Kreis"] = map_complete["RS"].str[0:5]
step1 = map_complete[["Kreis", "geometry"]]
Kreise = map_complete.dissolve(by="Kreis")


colors = 16
cmap = 'Blues'
figsize = (16, 10)
filter = 'RS'

title = 'Karte deutscher Bundesländer'
description = "Karte erstellt von Tobias Häfele"


figBL = Bundeslaender.plot(column=filter, cmap=cmap, figsize=figsize, scheme='equal_interval', k=colors, legend=True)

figBL.set_title(title, fontdict={'fontsize': 20}, loc='left')
figBL.annotate(description, xy=(0.1, 0.1), size=12, xycoords='figure fraction')

figBL.set_axis_off()
figBL.set_xlim([-1.5e7, 1.7e7])
figBL.get_legend().set_bbox_to_anchor((.12, .4))
figBL.get_figure()





'''



## add hover tools for Bundesländer
from bokeh.models import HoverTool
import matplotlib.pyplot as plt
from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure

hoverB = HoverTool(tooltips = [ ('Name','@GEN'), ("Bundeslandnummer", "@Bundesland")])
B = figure(title = 'Bundesländerkarte', plot_height = 600 , plot_width = 600, toolbar_location = None, tools = [hoverB])

## add hover tools for Kreise
hoverK = HoverTool(tooltips = [ ('Name','@GEN'), ("Bundeslandnummer", "@Bundesland")])
K = figure(title = 'Bundesländerkarte', plot_height = 600 , plot_width = 600, toolbar_location = None, tools = [hoverK])

## display both maps
show(K)
show(B)
'''

# Kreise.plot()
# Bundeslaender.plot()
# map_complete.plot()
