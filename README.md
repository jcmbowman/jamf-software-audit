# Jamf Software Audit

A simple python script and support files to simplify reporting of installed applications in Jamf Pro.

## Usage:

### Getting the application report from Jamf Pro:

In Jamf Pro go to the Computers > Search Inventory and click the "+ New" button to create a new advanced search.

Check the "Save this search" checkbox and then give the search a name (I went with "Application Report").

Choose a search criteria that will return all the computers you wish to monitor the aspplications of.

Configure the Display tab however you wish - this is irrelevant to the report that will be generated.

In the Reports tab set the File Format to .CSV, and set the Incventory Item to "Applications".

Save the search.

Go to the Reports tab and click on "Download Report" to get a .csv that contains a detailed list of all software installed on all the computers that are withing the search criteria.
You will use this .csv file to generate the more detailed software report.

If you wish, you can also set up email reporting to have Jamf Pro email you a copy of the report on the schedule you designate.

### Using the python script:

Open terminal, and cd to the diretory where this script and its supporting files live.

Run the script from the command line, providing the downloaded application report .csv as the first parameter to the script.

For example - if the file downloaded from Jamf Pro is named "251 Computers in Test.csv" this would be the command to run:
./ProcessJamfSoftwareReport.py ~/Downloads/251\ Computers\ in\ Test.csv

The script will run and output a .csv file that contains an extra column that you can use for sorting/filtering the application report.

### Using a Pivot Table to analyze the output CSV:

A Pivot Table is the easiest way I've found to analyze the data from this report. 

To create a pivot table in excel first, open the output CSV in Excel. 

When the file opens, click on any of the cells with data, then select all by pressing Command + A. 

Then go to the "Data" menu and select "Summarize with PivotTable". 

In the window that pops up leave the default settings (It should be set to create the pivot table in a new worksheet) and click OK.

It should present you with a pop-out window on the left titled "PivotTable Fields.

Drag "Application Title" to the Rows box.

Drag "Application Status" to the Columns box.

Drag "Computer Name" to the Values box.

If you want even more detailed information you can also optionally drag "Application Version" to the Rows box.

**Congatulations!!** You now have a pivot table that will allow you to filter based on app names, or based on the different application status types.

### Using the supplemental data txt files:

This script works by matching the software titles against one of several .txt files. Each .txt file expects one software title per row. It will ignore anything on a row after a # character, and it will strip any trailing spaces.

### Cleaning up the supplemental data files:

I have included another python script with this poject named "UnreferencedSoftwareSearch.py". Run this script with your Jamf Pro-created Application report csv as a parameter and it will return a list of all the software listed in the the supplemental data .txt files that is not in the current application report.







