

# Czech FOI Data 3D Plot 

The resulting 3D-Plots are  zoomable and rotatable HTML files. 
<br>You can download them here: [Result Folder](https://github.com/gitfrid/CzechFOI/tree/eec2d09b2b63c9c2f52d4e5a4ea79da2728db96e/3D%20Plot%20Results)

<br>**Example picture interactive 3D-Plot Czech FOI Data - all VX and UNVX**
<br>
_________________________________________
<br>
<img src="https://github.com/gitfrid/CzechFOI/blob/d6f3f69411efe25966cac1ad29dc1f34a268b596/3D%20Plot%20Results/Terra%203D%20Plot.png" width="600" height="auto">
<br>
Original Czech FOI-Data - fredom of information request - download from:
<br>https://github.com/PalackyUniversity/uzis-data-analysis/blob/main/data/Vesely_106_202403141131.tar.xz

<br>DB Browser for SQLite Version 3.13.0 download from:
<br>https://sqlitebrowser.org/dl/
<br>**.**
<br>
_________________________________________
<br>
The data in SQLite Database CZFOI.db were imported from the Vesely_106_202403141131_org.csv above.

Then the data from the SQLite database was processed, and the results were again exported to CSV files.
by using the SQL queries in the folder SQLQueries. This can all be processed in the SQLite query window.

Day of death in the SQLite queries are days counted from start date 2020.01.01,
since the integer number of days from 2020. 01.01 is easier to process in the phyton script than the date itself. 

Python and Visual Studio Code were used to create the phyton script for the 3D plot.

Phyton 3.12.5 to plot the csv data: 
https://www.python.org/downloads/

Visual Studio Code 1.92.2 to edit the phyton script (optional)
https://code.visualstudio.com/download

License: open source -GPL3 License
Disclaimer: The result has not been checked for errors.
