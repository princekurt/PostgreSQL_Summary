# PostgreSQL_Summary
This project uses the psycopg2 database from Python to run statistic reports on a PostgreSQL database. 

# Installation
This project requires a specific database to run named newsdata.sql. 
The database name is "news" with tables articles, authors, and log. 

# Database Structure
Database Name: News  
Table: articles  
author - integer (Foreign)
title - text  
slug - text  
lead - text  
body - text  
time - timestamp  
id - integer (Primary)  
  
Table: authors  
name - text  
bio - text  
id - text (Primary)  
  
Table log  
path - text  
ip - text  
method - text  
status - text  
time - timestamp  
id - int (Primary)  

# Usage 
Run the python folder with the sql folder within the same folder. It will then print out to the console the statistics 
of the file. This file is built using a linux environment and should be assumed to only work in one as well. 

This file was created using a vagrant environment running a virtualbox provided by Udacity.com. The newsdata.sql needs to be loaded by psql before the file will work. To run the program, run the main program db_summary using the python command. Due to size this database has not been provided in the github. However, a database created using the above specs will work out just fine. Note: It was developed and run on python 2.7.  

python db_summary
