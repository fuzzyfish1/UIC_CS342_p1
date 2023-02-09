SELECT 
	Station_ID, 
	sum(Num_Riders) as total
from Ridership

group by Station_ID
order by total desc

limit 10;
