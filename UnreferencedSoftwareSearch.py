#!/usr/bin/env python3

####
#
# UnreferencedSoftwareSearch.py
#
# Created 2023-06-15 by John Bowman
#
# Script to help keep our software lists trim - checks to see if any software
# titles in the software lists are not referenced in this month's CSV
#
####

### User-edited Variables ###


########## DO NOT EDIT BELOW THIS LINE ##########
import argparse, sys

# Initialize command line argument parser
parser = argparse.ArgumentParser()
 
# Adding command line arguments
parser.add_argument(
    "JamfCSV",
    help = "Jamf Application Report CSV file"
)
 
# Read arguments from command line
args = parser.parse_args()
 


# Read in all 3 Software lists

def readSoftwareFile (softwareFile):
    softwareList = []
    with open(softwareFile) as f:
        for line in f:
            if not line.startswith('#') and not line == '\n':
                softwareList.append(line.split('#',1)[0].strip())
        
    return softwareList

macOSbundledApps = readSoftwareFile("Software-macOSbundled.txt")
authorizedApps = readSoftwareFile("Software-Authorized.txt")
deprecatedApps = readSoftwareFile("Software-AuthorizedDeprecated.txt")
exceptionApps = readSoftwareFile("Software-ApprovedExceptions.txt")
blacklistApps = readSoftwareFile("Software-Blacklist.txt")


# Read in JamfCSV
import csv
appTitle = ''
appVersion = ''
outputData = []
with open(args.JamfCSV, encoding = "ISO-8859-1") as csvreadfile:
    readcsv = csv.reader(csvreadfile)
    for row in readcsv:
        appStatus = 'Unknown/Unauthorized'
        if not row[0] == '':
            appTitle = row[0]
        if not row[1] == '':
            appVersion = row[1]
        if macOSbundledApps.__contains__(appTitle):
            macOSbundledApps.remove(appTitle)
        if authorizedApps.__contains__(appTitle):
            authorizedApps.remove(appTitle)
        if deprecatedApps.__contains__(appTitle):
            deprecatedApps.remove(appTitle)
        if exceptionApps.__contains__(appTitle):
            exceptionApps.remove(appTitle)
        if blacklistApps.__contains__(appTitle):
            blacklistApps.remove(appTitle)


if macOSbundledApps:
    print ("macOS Bundled Apps:")
    print (macOSbundledApps)

if authorizedApps:
    print ("Authorized Apps:")
    print (authorizedApps)
if deprecatedApps:
    print ("Deprecated, but still Authorized Apps:")
    print (deprecatedApps)
if exceptionApps:
    print ("Apps granted special exceptions:")
    print (exceptionApps)
if blacklistApps:
    print ("Blacklisted Apps:")
    print (blacklistApps)

