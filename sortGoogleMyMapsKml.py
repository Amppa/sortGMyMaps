# -*- coding:utf-8 -*-
try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

INPUT_FILE_NAME = "input.kml"
OUTPUT_FILE_NAME = "output.kml"

namespace = "http://www.opengis.net/kml/2.2"
ET.register_namespace('', namespace)


def main():

	print("This is a script to sort GoogleMyMaps placemark by Latitude and Longitude")
	print("Please export GoogleMyMaps data to KML and rename as ", INPUT_FILE_NAME)
	
	tree = ET.parse(INPUT_FILE_NAME)
	root = tree.getroot()
	#namespace = tree.getroot().tag[1:].split("}")[0]
	
	doc = root.find("{%s}Document" % namespace)
	
	placeList = []
	placemarkToList(doc, placeList)
	#print(placeList)
	#printDbNameAndCoord(placeList)
	sortDb(placeList)
	#print(" ==== after ==== ")
	#printDbNameAndCoord(placeList)
	
	removePlacemarkElement(doc)
	appendElementFromListToElementTree(placeList, doc)
	
	tree.write(OUTPUT_FILE_NAME, "UTF-8", xml_declaration=True)
	print("All done")


def printChildElemTag(root):
	for elem in root:
		print(elem.tag)

def printElemDfs(root):
	for elem in root.iter():
		print(elem.tag, elem.attrib)


def printAllPlacemarkName(elem):
	for placemark in elem.findall("{%s}Placemark" % namespace):
		name = placemark.find('{%s}name' % namespace).text
		print(name)

def placemarkToList(elem, placeList):
	for placemark in elem.findall("{%s}Placemark" % namespace):
		name = placemark.find('{%s}name' % namespace).text
		
		point = placemark.find('{%s}Point' % namespace)
		coord_str = point.find('{%s}coordinates' % namespace).text
		
		coord_str = coord_str.strip()	#remove space or CRLF
		coord = coord_str.split(',')	#lat, long, alt = coord[0:3]
		coord_lat, coord_long = coord[0:2]
		#print(name, coord_lat, coord_long)
		
		placeList.append((name, float(coord_lat), float(coord_long), placemark))

def printDbNameAndCoord(placeList):
	for placeNode in placeList:
		print(placeNode[1], ", ", placeNode[2], ",\t", placeNode[0])	# Latitude, Longitude, name

# Latitude ========
# Longitude |||||||
def sortDb(placeList):
	placeList.sort(key = lambda s:s[1])	# sort by Latitude
	placeList.sort(key = lambda s:s[2])	# sort by Longitude


def removePlacemarkElement(elem):
	for placemark in elem.findall("{%s}Placemark" % namespace):
		elem.remove(placemark)

def appendElementFromListToElementTree(myList, myElemTree):
	for node in myList:
		myElemTree.append(node[3])		# copy element

if __name__ == "__main__":
	main()