#!/usr/bin/python
# Created by Jarle Fosen - jarlefosen@gmail.com
import json
import urllib2

url = "https://www.kimonolabs.com/api/1zpgdth4?kimmodify=1"
data = json.load(urllib2.urlopen(url))["results"]

week = data["menu_date"]
menu = data["menu_grouped"]

print week["week_name"]
print week["week_date"]

for day in menu:
    print "\n" + day["day_of_week"]
    for dish in day["dishes"]:
        line = "\t" + dish["type"] + "\t- " + dish["name"]
        print line.encode("utf-8")
