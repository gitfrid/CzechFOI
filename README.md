

# Czech
 Czech FOI 3D Terrain Plot

<br>**Interactive 3D-Plot CZ FOI Data all VX and UNVX**

<br>
<img src="https://github.com/gitfrid/CzechFOI/blob/461003cde1492dd4ff81a37831a0762ca449521a/3D%20Plot%20Results/TERRA_VX_UNVX.html" width="800" height="auto">
<br>
<br>
_________________________________________

Original Czech FOI-Data download from:
<br>https://github.com/PalackyUniversity/uzis-data-analysis/blob/main/data/Vesely_106_202403141131.tar.xz


DB Browser for SQLite Version 3.13.0 download from:
<br>https://sqlitebrowser.org/dl/


The Data in SQLite Database CZFOI.db were imported from the Vesely_106_202403141131_org.csv above.

Then the Data from the SQLite Datbase were processed and the results were again exported to CSV Files,
<br>by using the SQL queries the folder SQLQueries. This can all be processed in SQLite Query Window.

Day of death in the SQLite queries are days counted from  start date 2020.01.01,
<br>since a the integer number of days from 2020.01.01 is easyer to process in the phyton script then the date itself. 

Python and Visual Studio Code was used to create the phyton script for the 3D plot.

Phyton 3.12.5 to plot the csv Data: 
https://www.python.org/downloads/

Visual Studio Code 1.92.2 to edit the phyton script - optional:
https://code.visualstudio.com/download

 



