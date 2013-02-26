# Adding length tags

from maperipy import *
from maperipy.osm import *
import math

# Create a sorted list of main roads / nodes
# osmWayList = OsmData.load_pbf_file("D:\Tiles\OSM\israel_and_palestine.osm.pbf")

# Look for the first OSM map source.
for layer in Map.layers:
    if layer.layer_type == "OsmLayer":
        osmWayList = layer.osm

	for way in osmWayList.find_ways(lambda x : x.has_tag("highway")):
	    if way.nodes[0]!=way.nodes[way.nodes_count-1]:
		startx = osmWayList.node(way.nodes[0]).location.x
		starty = osmWayList.node(way.nodes[0]).location.y
		endx = osmWayList.node(way.nodes[way.nodes_count-1]).location.x
		endy = osmWayList.node(way.nodes[way.nodes_count-1]).location.y
		midx = (startx+endx)/2
		midy = (starty+endy)/2
		# Earth's circumference is about 40,000 km.
		# So 1 degree of longitude at the equator, or 1 degree of latitude, is about 40,000/360 = 110 km.
		distx = 40000*(endx-startx)/360 * math.cos(math.radians(midy))
		disty = 40000*(endy-starty)/360
		length = math.sqrt(distx*distx+disty*disty)
		osmWayList.way(way.id).set_tag("length", str(length))

# If there are no OSM map sources, report an error...
if osmWayList == None:
    raise AssertionError("There are no OSM map souces.")

# osmWayList.save_xml_file("D:\Tiles\OSM\israel_and_palestine_with_lengths.osm")
