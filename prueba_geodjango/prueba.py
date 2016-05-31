from django.contrib.gis.geos import Point
from world.models import *
import ee
import ee.mapclient
import json
ee.Initialize()

pais= WorldBorder.objects.get(name='Bolivia')
geometriaDict= json.loads(pais.mpoly.json)
bordePais = ee.Feature(geometriaDict)
bordePaisFC= ee.FeatureCollection([bordePais])

mosaicoArea= ee.ImageCollection('LANDSAT/LC8_L1T_TOA').filterDate('2015-06-01', '2015-09-01') .filterMetadata('CLOUD_COVER', 'less_than', 10).filterBounds(bordePaisFC).median().clip(bordePaisFC);

parametrosVisualizacion= {
    'landsat5':{
        'bands': 'B5,B4,B3',
        'min': '0',
        'max': '0.5',
        'gamma': '0.95,1.1,1'
    },
       'landsat8': {
        'bands': 'B6,B5,B4',
        'min': '0',
        'max': '0.5',
        'gamma': '0.95,1.1,1'
    },
    'landsat7': {
        'bands': ['B5', 'B4', 'B3'],
        'gain':[0.06,0.06,0.06]
    }
}
mapIdMosaico = mosaicoArea.getMapId(parametrosVisualizacion['landsat8']);
print(mapIdMosaico)
# ee.mapclient.centerMap(-66.14, -17.36, 6)
ee.mapclient.addToMap(mosaicoArea, parametrosVisualizacion['landsat8'], 'Mapa Landsat8', True)

# ee.mapclient.addToMap(bordePaisFC, {'color': '81BEF7'}, 'Borde area', False) 