# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:17:16 2016

@author: megan
"""
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import re
import codecs

# --------------------------------------------
# -- phase 1: get the page & save it to disk
# --------------------------------------------
# get the web page you are interested in parsing
targetURL = "http://www.flashresults.com/2013_Meets/outdoor/06-05-NCAA/live/027-1-01.htm"

try:
    print("opening target URL:", targetURL)
    htmlResult = urllib2.urlopen(targetURL).read()
except urllib2.HTTPError as error:
    print(error)

# save the html file locally
outfile = codecs.open('outfile.html', 'w')
outfile.write(str(htmlResult))
outfile.close()

# ---------------------------------------------------------------
# -- phase 2: read in the file and parse out the interesting bits
# ---------------------------------------------------------------
'''
test string:
<tr class='normal'><td>1</td><td>Abbey D'Agostino</td><td>DART</td><td><b>15:43.68</b></td><td><i>34.59 (34.59)</i></td><td><i>1:52.00 (1:17.41)</i></td><td><i>3:09.86 (1:17.87)</i></td><td><i>4:28.16 (1:18.30)</i></td><td><i>5:47.30 (1:19.14)</i></td><td><i>7:06.73 (1:19.44)</i></td><td><i>8:27.62 (1:20.90)</i></td><td><i>9:45.18 (1:17.56)</i></td><td><i>11:00.45 (1:15.28)</i></td><td><i>12:15.32 (1:14.87)</i></td><td><i>13:27.93 (1:12.61)</i></td><td><i>14:36.95 (1:09.03)</i></td><td><i>15:43.68 (1:06.74)</i></td></tr>

reg ex to grab out the pieces:
<tr class=\'(.*?)\'><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td><b>(.*?)<\/b><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><\/tr>
'''
infile = codecs.open('outfile.html', 'r', encoding='utf-8', errors='ignore')
for line in infile.read().split('</tr>'):
    weHaveAMatch = re.search('<tr class=\'(.*?)\'><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td><b>(.*?)<\/b><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td><td><i>(.*?) \((.*?)\)<\/i><\/td>', str(line))
    if weHaveAMatch:
        altOrNormal = weHaveAMatch.group(1)
        lineNum     = weHaveAMatch.group(2)
        personName  = weHaveAMatch.group(3)
        affiliation = weHaveAMatch.group(4)
        cumulative  = weHaveAMatch.group(5)
        r200m       = weHaveAMatch.group(6)
        r600m       = weHaveAMatch.group(8)
        r1000m      = weHaveAMatch.group(10)
        r1400m      = weHaveAMatch.group(12)
        r1800m      = weHaveAMatch.group(14)
        r2200m      = weHaveAMatch.group(16)
        r2600m      = weHaveAMatch.group(18)
        r3000m      = weHaveAMatch.group(20)
        r3400m      = weHaveAMatch.group(22)
        r3800m      = weHaveAMatch.group(24)
        r4200m      = weHaveAMatch.group(26)
        r4600m      = weHaveAMatch.group(28)
        r5000m      = weHaveAMatch.group(30)
        
        print("===")
        print("altOrNormal Row:", altOrNormal)
        print("line number:", lineNum)
        print("person Name:", personName)
        print("Affiliation:", affiliation)
        print("Cumulative Time:", cumulative)
        print("200m:", r200m)
        print("600m:", r600m)
        print("1000m:", r1000m)
        print("1400m:", r1400m)
        print("1800m:", r1800m)
        print("2200m:", r2200m)
        print("2600m:", r2600m)
        print("3000m:", r3000m)
        print("3400m:", r3400m)
        print("3800m:", r3800m)
        print("4200m:", r4200m)
        print("4600m:", r4600m)
        print("5000m:", r5000m)

