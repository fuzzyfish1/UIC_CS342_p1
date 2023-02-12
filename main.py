# -----------------------------------------------
#	Program 1: Analyzing CTA2 L data in Python
#		program takes user inputs to query SQLite Database

#	Course: CS341, Fall 2023. MWF 12pm lec

#	System: Ubuntu using terminal,
#		Python 3.10.6
#		sqlite3 3.37.2

#	Author: Zain Ali
# -----------------------------------------------

import sqlite3

# TODO: import matplotlib
import matplotlib.pyplot as plt

def riderShip(ascending=True, orderByName=True, limit=False):
	sql = "SELECT \n" \
		  "        sum(Num_Riders) as totalNumRiders\n" \
		  "from Ridership r\n" \
		  ";"

	total = float(dbCursor.execute(sql).fetchone()[0])

	sql = "SELECT \n" \
		  "        s.Station_Name, \n" \
		  "        sum(Num_Riders) as total\n" \
		  "from Ridership r\n" \
		  "inner join Stations s on s.Station_ID=r.Station_ID\n" \
		  "group by s.Station_ID\n" \
		  "order by "

	sql += "Station_Name " if orderByName else "total "
	sql += "asc\n" if ascending else "desc\n"

	sql += "limit 10;" if limit else ";"

	output = dbCursor.execute(sql)

	for row in output:
		print(row[0], ":", f"{row[1]:,}", f"({100.0 * row[1] / total:.2f}%)")

def opt1():
	sql = "SELECT\n" \
		  "Station_ID as ID,\n" \
		  "Station_Name as name\n" \
		  "from Stations\n" \
		  "group by name\n" \
		  "having name like ?\n" \
		  "order by name asc;\n"
	inp = input("\nEnter partial station name (wildcards _ and %): ")

	output = dbCursor.execute(sql, [inp]).fetchall()

	if len(output) == 0:
		print("**No stations found...")

	for row in output:
		print(row[0], ":", row[1])

def opt5():
	color = input("\nEnter a line color (e.g. Red or Yellow): ")

	sql = "SELECT \n" \
		  "        s.Stop_Name as name, \n" \
		  "        s.Direction as dirn, \n" \
		  "        s.ADA as access\n" \
		  "from Stops s \n" \
		  "inner join StopDetails sd on s.Stop_ID=sd.Stop_ID\n" \
		  "inner join Lines l on l.Line_ID=sd.Line_ID\n" \
		  "group by name\n" \
		  "having l.Color like ?\n" \
		  "order by l.Color asc;"

	output = dbCursor.execute(sql, [color]).fetchall()

	if len(output) == 0:
		print("**No such line...")

	for row in output:
		print(row[0], ":", "direction =", row[1], "(accessible?", "yes)" if row[2] == 1 else "no)")


def riderShipOverTime(month=True):
	# helps set format for query as year or month
	if month:
		t = "m"
	else:
		t = "Y"

	sql = "SELECT \n" \
		  "        STRFTIME(\"%" + t + "\", r.Ride_Date) as t,\n" \
									   "		 sum(Num_Riders) as ridersPerMonth\n" \
									   "from Ridership r\n" \
									   "group by STRFTIME(\"%" + t + "\", r.Ride_Date)\n" \
									   "order by t asc" \
									   ";"

	output = dbCursor.execute(sql).fetchall()

	x = []
	y = []

	for row in output:
		print(row[0], ":", f'{row[1]:,}')

		x.append(str(row[0])[-2:]) # forces only last 2 digits of year/month
		y.append(row[1])

	# plotting ---
	plot = input("Plot? (y/n) ")

	if plot == "y":

		timeFrame = "month" if month else "year"

		plt.xlabel(timeFrame)
		plt.ylabel("number of riders (x * 10 ^ 8)")
		plt.title(timeFrame + "ly ridership")

		plt.plot(x, y)
		plt.show()

def opt8():
	'''Inputs a year and the names of two stations (full or partial names), and then outputs the daily ridership at
	each station for that year. Since the output would be quite long, you should only output the first 5 days and
	last 5 days of data for each station (as shown below):
	Please enter a command (1-9, x to exit): 8
	Year to compare against? 2020
	Enter station 1 (wildcards _ and %): %uic%
	Enter station 2 (wildcards _ and %): %sox%
	Station 1: 40350 UIC-Halsted
	2020-01-01 958
	2020-01-02 2143
	2020-01-03 2215
	2020-01-04 1170
	2020-01-05 840
	2020-12-27 327
	2020-12-28 426
	2020-12-29 438
	2020-12-30 429
	2020-12-31 363
	Station 2: 40190 Sox-35th-Dan Ryan'''

	year = input("Year to compare against?")
	s1 = input("Enter station 1 (wildcards _ and %): ")
	s2 = input("Enter station 2 (wildcards _ and %): ")

	sql = "SELECT Ride_Date as date, Num_Riders\n"\
		  "FROM Ridership r\n" \
		  "inner join Stations s on s.Station_ID=r.Station_ID\n"\
		  "WHERE s.Station_Name like \"" + s1 + "\" AND STRFTIME(\"%Y\", date) = \"" + year + "\"\n"\
		  "ORDER BY date DESC\n"\
		  "LIMIT 5;\n"\
		  #"UNION ALL\n" \
		  #"SELECT * FROM\n" \
		  #"(SELECT Ride_Date as date, Num_Riders\n"\
		  #"FROM Ridership\n" \
		  #"inner join Stations s on s.Station_ID=r.Station_ID\n"\
		  #"having (s.Station_Name like " + s2+ " AND STRFIME(\"%Y\", date) = \"" + year + "\")\n"\
		  #"ORDER BY date ASC\n"\
		  #"LIMIT 5);\n"

	print(sql)

	output = dbCursor.execute(sql).fetchall()

	if len(output) == 0:
		print("**No such line...")




def opt9():
	pass


def handleMenu():
	print("Please enter a command (1-9, x to exit): ", end="")
	menu_option = input()

	if menu_option == "x":
		quit()

	elif menu_option == "1":
		opt1()

	elif menu_option == "2":
		print("** ridership all stations **")
		riderShip(ascending=True, orderByName=True, limit=False)

	elif menu_option == "3":
		print("** top-10 stations **")
		riderShip(ascending=False, orderByName=False, limit=True)

	elif menu_option == "4":
		print("** least-10 stations **")
		riderShip(ascending=True, orderByName=False, limit=True)

	elif menu_option == "5":
		opt5()

	elif menu_option == "6":
		riderShipOverTime()

	elif menu_option == "7":
		print("** ridership by year **")
		riderShipOverTime(month=False)

	elif menu_option == "8":
		opt8()

	elif menu_option == "9":
		opt9()

	else:
		print("**Error, unknown command, try again...\n")


def genStats():
	# sql by type of day
	sql = "SELECT \n" \
		  "        sum(Num_Riders) as totalNumRiders,\n" \
		  "		   Type_of_Day as tod,\n" \
		  "		   count(Num_Riders) as entryCount\n" \
		  "from Ridership r\n" \
		  "group by Type_of_Day\n" \
		  "order by tod asc" \
		  ";"

	weekTotals = dbCursor.execute(sql).fetchall()

	# sql for general ridership statistics
	sql = "SELECT \n" \
		  "        STRFTIME(\"%Y-%m-%d\",Min(Ride_Date)) as earliestDate,\n" \
		  "		   STRFTIME(\"%Y-%m-%d\",Max(Ride_Date)) as latestDate,\n" \
		  "		   count(Num_Riders) as entryCount,\n" \
		  "		   sum(Num_Riders) as total\n" \
		  "from Ridership r" \
		  ";"

	rideSummary = dbCursor.execute(sql).fetchone()

	earliestDate = rideSummary[0]
	latestDate = rideSummary[1]
	totalEntries = rideSummary[2]
	total = rideSummary[3]

	# not in ridership
	numStops = dbCursor.execute("SELECT count(distinct Stop_ID) from Stops;").fetchone()[0]
	numStations = dbCursor.execute("SELECT count(distinct Station_ID) from Stations;").fetchone()[0]

	print("** Welcome to CTA L analysis app **\n\n" +
		  "General stats:\n" +
		  "  # of stations: " + str(numStations) + "\n" +
		  "  # of stops: " + str(numStops) + "\n" +
		  "  # of ride entries: " + f'{totalEntries:,}\n' +
		  "  date range: " + earliestDate + " - " + latestDate + "\n" +
		  "  Total ridership: " + f'{total:,}' + "\n" +
		  "  Weekday ridership: " + f'{weekTotals[2][0]:,}' + " (" + f"{100.0 * weekTotals[2][0] / total:.2f}%)\n" +
		  "  Saturday ridership: " + f'{weekTotals[0][0]:,}' + " (" + f"{100.0 * weekTotals[0][0] / total:.2f}%)\n" +
		  "  Sunday/holiday ridership: " + f'{weekTotals[1][0]:,}' + " (" + f"{100.0 * weekTotals[1][0] / total:.2f}%)\n"
		  )


dbConn = sqlite3.connect("CTA2_L_daily_ridership.db")
dbCursor = dbConn.cursor()

genStats()

while True:
	handleMenu()
