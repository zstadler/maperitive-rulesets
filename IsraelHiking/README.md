Create Israel Hiking Map similar to Israel Trails Committee (ITC)
================================

The first part of following manual will explain how to create an Israel hiking style map (256x256 tiles).
The second part of the following manual will explain how to convert the map for offline use on an android device.

Maperitive (Windows only)
-------------------------

1. Download Maperitive from: http://maperitive.net/, extract it to a desired location
2. Go to https://github.com/HarelM/maperitive-rulesets/tree/master/IsraelHiking
  a. click on the Files tab
	b. click on the Zip with the cloud and arrow to download all the files
3. The zip file will contain some unnecessary folders and files, the only folder needed from this zip is called IsraelHiking, place it inside your Maperitive installation folder
 * you should now have a folder ...\<Maperitive Install folder>\IsraelHiking\
4. Download http://download.geofabrik.de/asia/israel-and-palestine-latest.osm.pbf and place it in the above folder
5. Open Maperitive program, click File -> Run Script... and choose IsraelHiking\IsraelHiking.mscript

This should generate 256x256 png tile files inside IsraelHiking\Tiles directory and should take long (about 2 hours or more).

MOBAC and Oruxmaps
-------------------------
1. In order to use an offline version of this map in an android device first install Oruxmaps from the play store, 
	https://play.google.com/store/apps/details?id=com.orux.oruxmaps
	this app is free of charge and does not have adds, it was not created by me but I felt the need to buy the "donate version."
2. Download MOBAC (MOBile Atlas Creator) from http://mobac.sourceforge.net/
2. Open IsraelHiking.xml file and change the <sourceFolder> tag to where the tiles were created (...\<Maperitive Install folder>\IsraelHiking\Tiles - full path).
3. Place the IsraelHiking.xml file in <MOBAC installtion folder>\mapsources\
4. Open MOBAC (it takes some time since it runs on java) and choose oruxmaps sqlite
5. On the left side under "Map Source" choose Isreal Hiking
6. Move zoom on the top of the screen to 7 and by mouse drag select the whole country (the selected area should be red)
7. Under "Zoom levels "check 7,8,..,15
8. Under "Atlas Content" set name to Hiking In Israel Maperitive and click on "Add Selection"
	this should result in adding the name to the tree, opening the tree should show the selected zoom levels
9. Click "Create Atlas"
10. A window should pop up with progress, make sure to check "ignore download errors", the operation should take about 3 hours (I think, I always run it overnight).
11. Once finished you should be able to find a folder under <MOBAC installation folder>\atlases\Israel Hiking_< Creation Date >\ called "Israel Hiking" 
12. Copy the "Israel Hiking" folder (not the one with the date) to you android device under /sdcard/oruxmaps/mapfiles
13. Enjoy, open a OSM account and add trails to make this map better :)


-------------------------
Created by Harel Mazor and Zeev Stadler 16.03.2013
