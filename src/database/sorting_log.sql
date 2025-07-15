CREATE TABLE IF NOT EXISTS SortingLog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME,
    object_type TEXT,
    status TEXT
);CREATE TABLE SortingLog (id INTEGER PRIMARY KEY AUTOINCREMENT, object_type TEXT, timestamp DATETIME);



#---cd ~/Downloads/Robotic-Sorting-System-main sqlite3 src/database/sorting_log.db < src/database/sorting_log.sql
#---ls -l src/database/sorting_log.db
