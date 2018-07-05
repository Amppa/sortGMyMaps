# sortGMyMaps

This python script can sort GoogleMyMaps's placemark by Latitude and Longitude

Google My Maps is a very useful service to sharing your place point to other.
But when there are too many placemarks in one map, it is wasting time to move from layer to layer.
The first thought is to sort placemark coordinate by Latitude and Longitude

(The second thought is grouping/clusting)

### Environment need
python 3.2+ (due to using iter() in ElementTree)


### Usage
1. Export GoogleMyMaps data to KML (not KMZ)
2. Change KML file name as "input.kml" (There is an example file)
3. Execute "sortGoogleMyMapsKml.py"
4. It should generate "output.kml"
5. Import "output.kml" into GoogleMyMaps


### Notice

1. Now it can handle layer(folder)

2. If you want to change the sorting order or reversing Latitude,
  you can edit function "sortPlaceByLatAndLong"

3. Besides place point, now it can handle polygon object
  But it only considers the first point(x,y) of polygon as its coordinate
