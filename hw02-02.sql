SELECT 
	s.Station_Name, 
	sum(Num_Riders) as total
from Ridership r
inner join Stations s on s.Station_ID=r.Station_ID
group by s.Station_ID
order by total desc

limit 10;
