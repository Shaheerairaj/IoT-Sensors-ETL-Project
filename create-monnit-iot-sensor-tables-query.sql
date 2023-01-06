CREATE TABLE vibration_sensor
(DataMessageGUID char(100) primary key,
SensorID int,
MessageDate float,
State int,
SignalStrength int,
Voltage float,
Battery int,
RawData varchar(200),
DisplayData varchar(200),
PlotValue float,
MetNotificationRequirements char(5),
GatewayID int,
DataValues varchar(200),
DataTypes varchar(200),
PlotValues varchar(200),
PlotLabels varchar(200),
SensorType char(50),
DataTimeStamp date)