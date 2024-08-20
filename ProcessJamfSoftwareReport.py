#!/usr/bin/env python3

####
#
# ProcessJamfSoftwareReport.py
#
# Created 2023-02-17 by John Bowman
#
# Script to process Jamf-generated software report into something usable by Excel.
#
# Compares against .txt files to set additional column
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
        computerName = row[2]
        if appTitle == 'Application Title':
            appStatus = 'Application Status'
        if macOSbundledApps.__contains__(appTitle):
            appStatus = 'macOS Bundled'
        if authorizedApps.__contains__(appTitle):
            appStatus = 'Authorized'
        if deprecatedApps.__contains__(appTitle):
            appStatus = 'Authorized but Deprecated'
        if exceptionApps.__contains__(appTitle):
            appStatus = 'Exception Documented'
        if blacklistApps.__contains__(appTitle):
            appStatus = 'Blacklisted'
        newRow = [appTitle,appVersion,computerName,appStatus]
        outputData.append(newRow)


# Output NewCSV
from datetime import datetime
outputCSVpath = "JamfSoftwareAudit_" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".csv"
print ("Output CSV: " + outputCSVpath)

with open(outputCSVpath, 'w+', newline='') as csvwritefile:
    csvwriter = csv.writer(csvwritefile, delimiter=',', quotechar='"')
    csvwriter.writerows(outputData)