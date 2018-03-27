import urllib2 as ul
import json
import csv
import math as m
import calendar
import time

def haversine(pos1, pos2):
    lat1 = float(pos1[0])
    long1 = float(pos1[1])
    lat2 = float(pos2[0])
    long2 = float(pos2[1])

    degree_to_rad = float(m.pi / 180.0)

    d_lat = (lat2 - lat1) * degree_to_rad
    d_long = (long2 - long1) * degree_to_rad

    a = pow(m.sin(d_lat / 2), 2) + m.cos(lat1 * degree_to_rad) * m.cos(lat2 * degree_to_rad) * pow(m.sin(d_long / 2), 2)
    c = 2 * m.atan2(m.sqrt(a), m.sqrt(1 - a))
    km = 6367 * c
    mi = 3956 * c

    return mi

urllink = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"

js_obj = json.load(ul.urlopen(urllink))
mags = []

menlo_park = [-122.1821900, 37.4538300]
for i in js_obj['features']:
    k = haversine(i['geometry']['coordinates'], menlo_park)
    if k <= 100:
        t = i['properties']['time']/1000 - calendar.timegm(time.gmtime())
        if abs(t) <= 7 * 24 * 3600:
            mags.append(i['properties']['mag'])
print max(mags)
