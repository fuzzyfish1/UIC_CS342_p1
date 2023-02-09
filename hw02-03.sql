SELECT
	strftime('%Y', Ride_Date) as year,
	sum(Num_Riders) as total
from Ridership

--declare @year as int
-- = cast( strftime('%Y', Ride_Date) as int)

group by year

having year >= '2011' and year <= '2020'


order by year desc

limit 10;
