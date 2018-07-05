# sortGMyMaps

This python script can sort GoogleMyMaps's placemark by Latitude and Longitude

Google My Maps is a very useful service to sharing your place point to other.
But when there are too many placemarks in one map, it is wasting time to move from layer to layer.
The first thought is to sort placemark coordinate by Latitude and Longitude

(The second thought is grouping/clusting)

### Environment need
python 3

### Usage
1. Export Google My Maps data to KML (not KMZ)
2. Change KML file name as "input.kml" (There is a example file)
3. Execute "sortGoogleMyMapsKml.py"
4. It should generate "output.kml"
5. Inport "output.kml" into Google My Maps new layer

### Notice
1. This does not support multi layers yet.
2. If you want to change the sorting order or reverse, you can edit function "sortPlaceByLatAndLong"
