# creates OSM file with horizontal and vertical lines
# you have the permission to do what ever you want with this code...
#
# 2013/03/02 Harel Mazor

from maperipy import *
from maperipy.osm import *
import math

#-------- Defines ---------
dbLatitudeStart = 29
dbLatitudeEnd = 34
#Latitude: 1 deg = 110.54 km

dbLongitudeStart = 34
dbLongitudeEnd = 36
#Longitude: 1 deg = 111.320*cos(latitude) km

sFileName = 'IsraelHiking\grid.osm'
#---------------------------

osmFile = open(sFileName, 'w')
iId = 0
# writing osm header
osmFile.write('<?xml version="1.0" encoding="utf-8"?>' + "\n")
osmFile.write('<osm version="0.5" generator="CreateGridOsm.py">' + "\n")
#------------------------------------------------------------

# Adding  horizontal lines
dbLat = dbLatitudeStart
while (dbLat <= dbLatitudeEnd) :
  iId = iId - 1
	dbLon = dbLongitudeStart
	osmFile.write('  <node id="' + str(iId) + '" visible="true" lat="' + str(dbLat) + '" lon="' + str(dbLon) + '" />' + "\n")
	iId = iId - 1
	dbLon = dbLongitudeEnd
	osmFile.write('  <node id="' + str(iId) + '" visible="true" lat="' + str(dbLat) + '" lon="' + str(dbLon) + '" />' + "\n")
	iId = iId - 1
	osmFile.write('  <way id="' + str(iId) + '" visible="true">' + "\n")
	osmFile.write('    <nd ref="' + str(iId + 1) + '" />' + "\n")
	osmFile.write('    <nd ref="' + str(iId + 2) + '" />' + "\n")
	osmFile.write('    <tag k="gpxtrack" v="grid"/>' + "\n")
	osmFile.write('  </way>' + "\n")
	#Latitude: 1 deg = 110.54 km
	dbLat = dbLat + (1/110.54)
	
# Adding vertical lines
dbLon = dbLongitudeStart
while (dbLon <= dbLongitudeEnd) :
	iId = iId - 1
	dbLat = dbLatitudeStart
	osmFile.write('  <node id="' + str(iId) + '" visible="true" lat="' + str(dbLat) + '" lon="' + str(dbLon) + '" />' + "\n")
	iId = iId - 1
	dbLat = dbLatitudeEnd
	osmFile.write('  <node id="' + str(iId) + '" visible="true" lat="' + str(dbLat) + '" lon="' + str(dbLon) + '" />' + "\n")
	iId = iId - 1
	osmFile.write('  <way id="' + str(iId) + '" visible="true">' + "\n")
	osmFile.write('    <nd ref="' + str(iId + 1) + '" />' + "\n")
	osmFile.write('    <nd ref="' + str(iId + 2) + '" />' + "\n")
	osmFile.write('    <tag k="gpxtrack" v="grid"/>' + "\n")
	osmFile.write('  </way>' + "\n")
	#Longitude: 1 deg = 111.320*cos(latitude) km, setting latitude at 35 degrees
	dbLatMiddle = (dbLatitudeStart + dbLatitudeEnd) / 2
	dbLon = dbLon + (1/(111.320*math.cos(dbLatMiddle)))
#------------------------------------------------------------

# writing osm fotter
osmFile.write('</osm>')
osmFile.close()
