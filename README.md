

# Czech
 Czech FOI 3D Terrain Plot


Original Czech FOI-Data download from: 

https://github.com/PalackyUniversity/uzis-data-analysis/blob/main/data/Vesely_106_202403141131.tar.xz


DB Browser for SQLite Version 3.13.0 download from:
https://sqlitebrowser.org/dl/


The Data in SQLite Database CZFOI.db were imported from the Vesely_106_202403141131_org.csv above

Then the Data from the SQLite Datbase were processed and the results were again exported to CSV Files,
by using the SQL queries the folder SQLQueries. This can all be processed in SQLite Query Window.

Day of death in the SQLite Queries ar days counted from the start date 2020.01.01, 
since a the integer number of Days from 2020.01.01 is easyer to process in the phyton script then the Date itself. 

Python and Visual Studio Code was used to create the phyton script for the 3D plot.

Phyton 3.12.5 to plot the csv Data: 
https://www.python.org/downloads/

Visual Studio Code 1.92.2 to edit the phyton script - optional:
https://code.visualstudio.com/download

 



