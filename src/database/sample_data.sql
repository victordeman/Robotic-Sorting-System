INSERT INTO SortingLog (timestamp, object_type, status) VALUES
('2025-07-15 10:00:00', 'Red', 'Detected'),
('2025-07-15 10:01:00', 'Blue', 'Detected'),
('2025-07-15 10:02:00', 'None', 'Fault');



#--For testing. "Take Note"

#---Apply the sample data:
#---sqlite3 src/database/sorting_log.db < src/database/sample_data.sql



#---Verify:
#---sqlite3 src/database/sorting_log.db "SELECT * FROM SortingLog;"

#--expected output:
#--1|2025-07-15 10:00:00|Red|Detected
#--2|2025-07-15 10:01:00|Blue|Detected
#--3|2025-07-15 10:02:00|None|Fault
