SELECT
	Stop_ID as ID,
	Stop_Name as name
from Stops

join Stations where Stops.Station_ID=Stations.Station_ID
group by name
having name like '%Sheridan%'


order by name asc

limit 10;
