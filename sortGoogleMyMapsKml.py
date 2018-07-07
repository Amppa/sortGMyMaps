# -*- coding:utf-8 -*-
try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

INPUT_FILE_NAME = "input3.kml"
OUTPUT_FILE_NAME = "output.kml"

namespace = "http://www.opengis.net/kml/2.2"
ET.register_namespace('', namespace)


def main():

	print("This is a tool to sort GoogleMyMaps's placemarks by thier coordinate")
	print("This version only sort in each layer(folder), so it won't change the layer's struction.\n")
	print("Please export GoogleMyMaps file to KML and rename as '" + INPUT_FILE_NAME + "'")
	
	tree = ET.parse(INPUT_FILE_NAME)
	root = tree.getroot()
	#namespace = tree.getroot().tag[1:].split("}")[0]
	
	doc = root.find("{%s}Document" % namespace)
	sortPlacemarkOfAllFolder(doc)

	tree.write(OUTPUT_FILE_NAME, "UTF-8", xml_declaration=True)
	print("Output done, please import '" + OUTPUT_FILE_NAME + "' into GoogleMyMaps.")


def printChildElmtTag(root):
	for elmt in root:
		print(elmt.tag)

def printElmtDfs(root):
	for elmt in root.iter():
		print(elmt.tag, elmt.attrib)

def printAllPlacemarkName(folder):
	for placemark in folder.findall("{%s}Placemark" % namespace):
		name = placemark.find('{%s}name' % namespace).text
		print(name)

def sortPlacemarkOfAllFolder(doc):

	folderGroup = doc.findall("{%s}Folder" % namespace)
	if folderGroup is None:
		sortPlacemarkInFolder(doc)
	else:
		for folder in folderGroup:
			sortPlacemarkInFolder(folder)
			print('.', end='')

def sortPlacemarkInFolder(folder):
	placeDict = []
	parserPlacemarkToDict(folder, placeDict)
	#printNameAndCoord(placeDict)
	sortDb(placeDict)
	#print(" ==== after ==== ")
	#printNameAndCoord(placeDict)

	removePlacemarkElmt(folder)
	appendPlacemarkElmt_fromDistToFolder(placeDict, folder)

def parserPlacemarkToDict(folder, placeDict):
	for placemark in folder.findall("{%s}Placemark" % namespace):
		name = placemark.find('{%s}name' % namespace).text
		for coordElmt in placemark.iter('{%s}coordinates' % namespace):
			coord_str = coordElmt.text
		
		coord_str = coord_str.strip()	#remove space or CRLF
		coord = coord_str.split(',')	#Longitude, Latitude, alt = coord[0:3]
		coord_long, coord_lat = coord[0:2]
		
		placeDict.append({'name':name, 'x':float(coord_long), 'y':float(coord_lat), 'elmt':placemark})

def printNameAndCoord(placeDict):
	for p in placeDict:
		print(p['x'], ", ", p['y'], ",\t", p['name'])

# Latitude ======== y
# Longitude ||||||| x
def sortDb(placeDict):
	placeDict.sort(key = lambda s:s['x'])
	placeDict.sort(key = lambda s:s['y'])


def removePlacemarkElmt(folder):
	for placemark in folder.findall("{%s}Placemark" % namespace):
		folder.remove(placemark)

def appendPlacemarkElmt_fromDistToFolder(myList, folder):
	for node in myList:
		folder.append(node['elmt'])		# copy element

if __name__ == "__main__":
	main()