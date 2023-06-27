# IoT-Sensors-ETL-Project #
## Objective ##
i. Build an ETL pipeline using live IoT data  
ii. Understand CRON jobs  
iii. Understand building relational databases and tables  
iv. Understand basics of querying and inserting data into relational tables  

## Project Description ##  
Live IoT sensors are deployed on site which monitor the evironmental conditions of a space (CO2 levels, humidity levels, temperature) as well as capture key operational data of FAHUs (differential pressure in supply and return comapartments, vibrations of the motors).  

The goal of the project is to build a live ETL pipeline to capture the data received by these sensors.  

The ETL script is written entirely in Python and the script was scheduled using windows task manager set to run hourly.  

The script was sitting on a local machine connected to the internet running non-stop.  

### Issues faced ###  
The API specifies that a date range needs to be given to determine the period between which values to call. Since the sensors retreive data on an hourly basis, there could be some delay before the new values are entered and terefore leads to either missing values for the hour, or at times duplicates entered into the table.  

### Future Improvements ###  
i. A quality check needs to eb defined to remove duplicates before they are entered into the table to toackle the issue mentioned above.  
ii. Build dashboards and visuals to display the data being sent by the sensors.  
iii. Possibly use predictive analytics to predict and prevent breakdowns of the asset using the motor vibration and differential pressure sensor data (maybe even conditions of the room/space).
